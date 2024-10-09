from django import forms
from .models import Food
from django import forms

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'description', 'price', 'day_of_week']

