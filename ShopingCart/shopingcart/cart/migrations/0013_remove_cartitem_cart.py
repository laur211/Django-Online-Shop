# Generated by Django 3.0.1 on 2020-03-22 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_auto_20200322_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
    ]
