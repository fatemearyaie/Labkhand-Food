from django import forms
from .models import Food
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'description', 'price', 'day_of_week']



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

