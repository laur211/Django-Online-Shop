# Generated by Django 3.0.1 on 2020-03-22 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_remove_cart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cartitems',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
            preserve_default=False,
        ),
    ]