from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('foods/', views.foods, name='foods'),
    path('foods/<str:day>/', views.food_list, name='food_list'),
    path('adminpanel/', views.admin_panel, name='admin_panel'),
    path('add_to_cart/<slug:food_slug>/', views.add_to_cart_ajax, name='add_to_cart_ajax'),
    path('cart/', views.cart_view, name='cart_view'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('finalize-order/', views.finalize_order, name='finalize_order'),
    path('addfood/', views.add_food, name='add_food'),
    path('success/', views.success_view, name='success_url'),
    path('delete_all_foods/', views.delete_all_foods, name='delete_all_foods'),
    path('finalize/', views.success_finalize, name='success_finalize'),
    path('adminreport/', views.admin_report, name='admin_report'),
    path('logout/', views.user_logout, name='logout'),
]
