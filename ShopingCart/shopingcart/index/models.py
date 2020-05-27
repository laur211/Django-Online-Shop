from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField(blank=False)
    image=models.ImageField(blank=False, upload_to="product_image")
    quantity=models.IntegerField(blank=False,null=False,default=1)
    available=models.BooleanField(default=True)
    def __str__(self):
        return self.name