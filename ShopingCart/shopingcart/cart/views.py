from django.shortcuts import render, HttpResponseRedirect
from .models import Cart, CartItem
from index.customdecorators import login_required
from index.models import Product
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
# Create your views here.


def sample_view(request):
    current_user = request.user
    return current_user.id

# @login_required
def cart_view(request):
    cart=Cart.objects.all()
    if request.user.is_authenticated:
        user = User.objects.get(id=sample_view(request))
        usercart = user.cart
        costs=[]
        for i in CartItem.objects.all():
            if usercart.id == i.cart.id:
                costs.append(i.itemtotal)
        usercart.total=sum(costs)
        usercart.save()
        try:
            cartitem=CartItem.objects.all()
        except:
            cart=Cart.objects.all()
        return render(request, "cart/cart.html", {"cart": cart, "cartitem": cartitem})
    else:
        cart=Cart.objects.all()
        cartitem=CartItem.objects.all()
        return render(request, "cart/cart.html" , {"cart":cart, "cartitem": cartitem})









@login_required
def update_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    user=User.objects.get(id=sample_view(request))
    price=product.price
    if product.available:
        if product in user.cart.products.all():
            cartitem = CartItem.objects.get(item=product, cart=user.cart)
            if product.quantity > cartitem.quantity:
                cartitem.quantity += 1
                cartitem.itemtotal = price * cartitem.quantity
                messages.success (request, f"Quantity increased for the product: {cartitem.item.name}")
                cartitem.save()
            else:
                messages.info (request, f"The maxim quantity of the product {product.name} has been reached")
        else:
            cartitem = CartItem.objects.create(item=product, cart=user.cart)
            if product.quantity >= cartitem.quantity:
                cartitem.itemtotal = product.price
                user.cart.products.add(product)
                cartitem.itemtotal = product.price
                messages.success(request, f"The product {cartitem.item.name} has been added to your cart")
                cartitem.save()
            else:
                messages.info(request, f"The maxim quantity of the product {product.name} has been reached")
    else:
        messages.info(request, f"The product {product.name} is unavailable")
    return HttpResponseRedirect(reverse("shop-home"))







@login_required
def increase_quantity(request, product_id):
    user = User.objects.get(id=sample_view(request))
    product = Product.objects.get(id=product_id)
    cartitem = CartItem.objects.get(item=product, cart=user.cart)
    price = product.price
    if product.available:
        if product.quantity > cartitem.quantity:
            cartitem.quantity += 1
            cartitem.itemtotal = price * cartitem.quantity
            messages.success (request, f"Quantity increased for the product: {cartitem.item.name}")
            cartitem.save()
        else:
            messages.info(request, f"The maxim quantity of the product {cartitem.item.name} has been reached")
    else:
        messages.info(request, f"The product {product.name} is unavailable")
    return HttpResponseRedirect(reverse("cart"))

@login_required
def decrease_quantity(request,product_id):
    user = User.objects.get(id=sample_view(request))
    product = Product.objects.get(id=product_id)
    cartitem = CartItem.objects.get(item=product, cart=user.cart)
    price = product.price
    cartitem.quantity -= 1
    cartitem.itemtotal = price * cartitem.quantity
    cartitem.save()
    if cartitem.quantity == 0:
        user.cart.products.remove(product)
        try:
            cartitem = CartItem.objects.get(item=product, cart=user.cart)
            cartitem.delete()
        except:
            pass
        finally:
            pass
        messages.success(request, f"The product {cartitem.item.name} has been removed from your cart")
    return HttpResponseRedirect(reverse("cart"))

def remove_item(request,product_id):
    user=User.objects.get(id=sample_view(request))
    product = Product.objects.get(id=product_id)
    user.cart.products.remove(product)
    try:
        cartitem=CartItem.objects.get(item=product, cart=user.cart)
        cartitem.delete()
    except:
        pass
    finally:
        pass
    messages.success(request, f"The product {product.name} has been removed from your cart")
    product.save()
    return HttpResponseRedirect(reverse("cart"))

