
from django.urls import path, include
from .views import AddProductFormView, view, DeleteProduct, UpdateProduct, search


urlpatterns = [
    path("", view,name="shop-home"),
    path("s/", search,name="search"),
    path("add_product/", AddProductFormView, name="add_product"),
    path("delete_product/<int:product_id>",DeleteProduct,name="delete_product"),
    path("update_product/<int:product_id>",UpdateProduct,name="update_product"),

]