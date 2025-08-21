from django import forms
from .models import Food
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import GroupFoodPrice
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Food, GroupFoodPrice

# فرم غذا
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'description', 'price', 'day_of_week']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
        }

# فرم قیمت گروه برای غذا
class GroupFoodPriceForm(forms.ModelForm):
    class Meta:
        model = GroupFoodPrice
        fields = ['group', 'food', 'price']
        widgets = {
            'group': forms.Select(attrs={'class': 'form-control', 'style': 'z-index:2000;'}),
            'food': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2',  # ← کلاس select2
                'style': 'width:100%;'  # حتماً عرض 100٪
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "groups")

# فرم ایجاد گروه جدید
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
