from django.db import models
from index.models import Product
from django.contrib.auth.models import User
# Create your models here.



class Cart(models.Model):
    total=models.DecimalField(max_digits=1000,default=0.00,decimal_places=2)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    products=models.ManyToManyField(Product, blank=True)

    def __unicode__(self):
        return self.id

class CartItem(models.Model):
    item=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    itemtotal= models.IntegerField(null=True)

    def __unicode__(self):
        return self.item.id

