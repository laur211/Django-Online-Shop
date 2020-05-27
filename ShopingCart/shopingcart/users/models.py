from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="user_photo",default="users_default.jpg")
    def __str__(self):
        return self.user.username




