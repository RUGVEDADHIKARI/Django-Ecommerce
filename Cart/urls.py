from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<uid>/', views.add_to_cart, name='add_to_cart'),
    path('cart_page/', views.cart_page, name='cart_page'),
    path('remove_cart_item/<uid>/', views.remove_cart_item, name='remove_cart_item'),
    path('remove_coupon/<cart_id>/', views.remove_coupon, name='remove_coupon'),
]