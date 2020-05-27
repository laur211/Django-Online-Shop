from django.shortcuts import render, redirect
from django.contrib import messages

def user_permision(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        elif request.user.groups.all()[0].name == "Customers":
            messages.warning(request, "You don't have access to this page")
            return redirect ("shop-home")
        elif request.user.groups.all()[0].name == "Staff":
            return view_func(request, *args, **kwargs)
        else:
            pass
    return wrapper_func


def login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(request, "You need to be logged in to perfom this action")
            return redirect("login")
    return wrapper_func
