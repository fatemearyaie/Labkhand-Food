from django.contrib import admin
from .models import Reservation, Food, Card, FoodGroup, GroupFoodPrice


# نمایش قیمت‌های گروهی داخل صفحه‌ی غذا
class GroupFoodPriceInline(admin.TabularInline):
    model = GroupFoodPrice
    extra = 1   # تعداد فرم‌های خالی
    autocomplete_fields = ['group']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'jdate', 'price', 'day_of_week')
    search_fields = ('food_name',)
    list_filter = ('day_of_week',)
    inlines = [GroupFoodPriceInline]


@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(GroupFoodPrice)
class GroupFoodPriceAdmin(admin.ModelAdmin):
    list_display = ('food', 'group', 'price')
    list_filter = ('group', 'food')
    search_fields = ('food__food_name', 'group__name')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'quantity', 'jdate', 'is_completed')
    list_filter = ('is_completed', 'day_of_week')
    search_fields = ('user__username', 'food__food_name')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('food', 'user', 'quantity', 'jdate')
    search_fields = ('user__username', 'food__food_name')
