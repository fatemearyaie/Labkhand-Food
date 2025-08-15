from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .models import Food, Card, Reservation
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse
from django.contrib import messages
from decimal import Decimal, InvalidOperation


# render pages
@login_required
def foods(request, pk):
    food = Food.objects.get(id=pk)
    return render(request, 'foods.html', {'food':food})
def admin_panel(request):
    return render(request, 'admin_panel.html', {})
def foods(request):
    return render(request, 'index.html', {})
def success_view(request):
    return render(request, 'success.html')
def success_finalize(request):
    return render(request, 'finalize.html')
def login(request):
    return render(request, 'login.html')

# login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('admin_panel')
            else:
                return redirect('foods')
        else:
            return render(request, 'login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است.'})
    return render(request, 'login.html')

# to show list of food in index
def food_list(request, day):  
    foods = Food.objects.filter(day_of_week=day)
    return render(request, 'index.html', {'foods': foods, 'day': day})


# view cart options
@login_required
def cart_view(request):
    cart_items = Card.objects.filter(user=request.user)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
    })

@login_required
def add_to_cart_ajax(request, food_slug):
    if request.method == 'POST':
        try:
            user = request.user
            data = json.loads(request.body)  
            quantity = int(data.get('quantity', 1))  
            food_item = Food.objects.get(slug=food_slug)
            day = data.get('day')  # گرفتن روز از داده‌ها

            # ابتدا باید یک سبد خرید برای کاربر چک کنیم
            cart_item, created = Card.objects.get_or_create(user=user, food=food_item, day=day)

            if created:
                cart_item.quantity = quantity  
            else:
                cart_item.quantity += quantity  

            cart_item.save()

            cart_items = Card.objects.filter(user=user)
            item_count = cart_items.count()

            return JsonResponse({'status': 'success', 'item_count': item_count})
        except Food.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Food item not found!'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'failed'}, status=400)

# remove some thing from cart
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Card, id=item_id, user=request.user)
    cart_item.delete()
    return HttpResponseRedirect(reverse('cart_view'))

# submit the reservation
@login_required
def complete_purchase(request):
    user = request.user
    cart_items = Card.objects.filter(user=user) 

    if cart_items.exists():
        for item in cart_items:
            item.is_purchased = True
            item.save()

        cart_items.delete()

        messages.success(request, "خرید شما با موفقیت نهایی شد.")
    else:
        messages.error(request, "سبد خرید شما خالی است!")
    return redirect('cart_view')

# save data to database
@login_required
def finalize_order(request):
    if request.method == "POST":
        cart_items = Card.objects.filter(user=request.user)
        for item in cart_items:
            
            reservation = Reservation.objects.create(
                user = request.user,
                food = item.food,
                quantity = item.quantity,
                day_of_week = item.food.day_of_week, 
            )
        cart_items.delete()
        return redirect('success_finalize')
    return redirect('cart')

# add new food in admin panel
@login_required
def add_food(request):
    if request.method == 'POST':
        for i in range(1, 8):
            food_name = request.POST.get(f'food{i}')
            day_of_week = request.POST.get(f'day{i}')

            if food_name and day_of_week:
                Food.objects.create(
                    food_name=food_name,
                    day_of_week=day_of_week
                )

        return redirect('success_url')
    else:
        context = {
            'food_range': range(1, 8) 
        }
        return render(request, 'admin_panel.html', context)
    
# delete all foods+reservations from database
def delete_all_foods(request):
    if request.method == 'POST':
        Food.objects.all().delete()
        Reservation.objects.all().delete()
        return redirect('add_food') 
    return HttpResponse(status=405)

def admin_report(request):
    reservations = Reservation.objects.all()
    total_quantity = calculate_total_quantity(reservations)

    context = {
        'reservations': reservations,
        'total_quantity': total_quantity,
    }
    return render(request, 'admin_report.html', context)


def calculate_total_quantity(reservations):
    return sum(reservation.quantity for reservation in reservations)
