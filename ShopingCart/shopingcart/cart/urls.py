
from django.urls import path, include
from . import views

urlpatterns = [
    path("cart/", views.cart_view, name="cart"),
    path("update_cart/<int:product_id>", views.update_cart,name="update_cart"),
    path("remove_item/<int:product_id>", views.remove_item,name="remove_item"),
    path("increase_quantity/<int:product_id>", views.increase_quantity,name="increase_quantity"),
    path("decrease_quantity/<int:product_id>", views.decrease_quantity,name="decrease_quantity"),
]
