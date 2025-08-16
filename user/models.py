from django.db import models
import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, User
from extensions.utils import jalaliConvertor
from django.utils import timezone


# Food model
class Food(models.Model):
    slug = models.PositiveIntegerField(unique=True, blank=True, null=True)
    food_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    CHOICE = [
        ('Sun', 'یکشنبه'),
        ('Mon', 'دوشنبه'),
        ('Tue', 'سه شنبه'),
        ('Wed', 'چهارشنبه'),
        ('Thu', 'پنجشنبه'),
        ('Fri', 'جمعه'),
        ('Sat', 'شنبه'),
    ]
    day_of_week = models.CharField(max_length=3, choices=CHOICE, default='Sat') 
    datetime = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # فقط در صورتی که slug وجود ندارد، مقداردهی شود
            last_slug = Food.objects.order_by('slug').last()
            self.slug = (last_slug.slug + 1) if last_slug else 1  # ایجاد slug خودکار
        super().save(*args, **kwargs)
    @property
    def jdate(self):
        return jalaliConvertor(self.datetime)
    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذاها'

class Reservation(models.Model):
    CHOICE = [
        ('Sun', 'یکشنبه'),
        ('Mon', 'دوشنبه'),
        ('Tue', 'سه شنبه'),
        ('Wed', 'چهارشنبه'),
        ('Thu', 'پنجشنبه'),
        ('Fri', 'جمعه'),
        ('Sat', 'شنبه'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateField(null=True, blank=True)
    day_of_week = models.CharField(max_length=20, default='sat', choices=CHOICE) 
    is_completed = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.user.username} - {self.food.food_name} - {self.quantity} - {'Completed' if self.is_completed else 'Pending'}"
    @property
    def jdate(self):
        return jalaliConvertor(self.order_date)
    def save(self, *args, **kwargs):
        if self.order_date and self.order_date.strftime('%a') != self.food.day_of_week:
            raise ValueError("Order date does not match the food's day of the week")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = 'رزروها'


class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # تغییر به ForeignKey
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    datetime = models.DateTimeField(auto_now_add=True)
    day = models.CharField(max_length=10, default='sat')

    def __str__(self):
        return f"{self.food} - {self.user.username} ({self.day})"
    def jdate(self): # this is a method to use jalali date in app
        return jalaliConvertor(self.datetime)
    class Meta:
        verbose_name = 'کارت'
        verbose_name_plural = 'کارت ها'
