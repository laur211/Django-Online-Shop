# Generated by Django 3.0.1 on 2020-03-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200308_1157'),
        ('cart', '0028_auto_20200328_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='index.Product'),
        ),
    ]