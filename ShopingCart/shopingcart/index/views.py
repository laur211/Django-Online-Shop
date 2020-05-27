from django.shortcuts import render, redirect
from .models import Product
from .Forms import ProductForm
from .customdecorators import user_permision, login_required
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def view(request):
    if request.user.is_authenticated:
        for product in Product.objects.all():
            if product.quantity > 0 :
                product.available = True
            else:
                product.available = False
            product.save()
        if request.user.groups.all()[0].name == "Staff":
            Products_list = Product.objects.all()
        elif request.user.groups.all()[0].name == "Customers":
            Products_list = Product.objects.filter(available=True)
    else:
        Products_list = Product.objects.filter(available=True)
    return render(request, "index/index.html", {"Products_list": Products_list})

def search(request):
    querry=request.GET.get("q")
    order=Product.objects.filter(Q(name__icontains=querry))
    return render(request, "index/index.html", {"Products_list": order})


@user_permision
@login_required
def AddProductFormView(request):
    if request.method=="POST":
        productform=ProductForm(request.POST, request.FILES)
        if productform.is_valid():
            productform.save()
            return redirect ("shop-home")

    else:
        productform=ProductForm()
    return render (request, "index/productform.html", {"productform":productform})


@login_required
@user_permision
def UpdateProduct(request,product_id):
    product=Product.objects.get(id=product_id)
    productform=ProductForm(request.POST,request.FILES,instance=product)
    if productform.is_valid():
        productform.save()
        messages.success(request, f"The product {product.name} has been update")
        return redirect("shop-home")
    else:
        productform = ProductForm(instance=product)
    return render(request, "index/productform.html", {"productform": productform})


@login_required
@user_permision
def DeleteProduct(request, product_id):
    product=Product.objects.get(id=product_id)
    messages.success(request, f"The product {product.name} has been deleted")
    product.delete()
    return redirect("shop-home")

