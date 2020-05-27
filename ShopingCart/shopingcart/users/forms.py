from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile




class RegisterForm(UserCreationForm):
    email=forms.EmailField(max_length=300)

    class Meta:
        model=User
        fields=["username","email","password1","password2"]
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email"]
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["image"]
