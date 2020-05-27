from django.shortcuts import render, redirect
from .forms import RegisterForm, UserCreationForm,UpdateProfileForm, UserUpdateForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            request.user.groups.add(2)
            messages.success (request, f"Account created for {username}")
            return redirect("shop-home")
    else:
        form=RegisterForm()
    return render(request, "users/register.html", {"form":form})


@login_required
def profile(request):
    if request.method=="POST":
        user_form=UserUpdateForm(request.POST,instance=request.user)
        update_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and update_form.is_valid():
            user_form.save()
            update_form.save()
            return redirect("profile")
    else:
        user_form = UserUpdateForm( instance=request.user)
        update_form = UpdateProfileForm( instance=request.user.profile)

    update={"user_form":user_form,
            "update_form":update_form}

    return render(request,"users/profile.html",update)


def logout_view(request):
    logout(request)
    messages.success(request, "You had been logged out")
    return redirect("login")
