# Generated by Django 3.0.1 on 2020-03-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200308_1157'),
        ('cart', '0014_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='index.Product'),
        ),
    ]
