# Generated by Django 3.0.1 on 2020-03-22 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cartitem_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cartitems',
        ),
    ]
