from django import forms
from .models import Food
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'description', 'price', 'day_of_week']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group



# فرم کاربر
class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'id': 'id_groups'})  # ← حتماً id بذارید
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "groups")


# فرم گروه جدید
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']