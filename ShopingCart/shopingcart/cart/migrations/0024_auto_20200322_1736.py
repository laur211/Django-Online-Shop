# Generated by Django 3.0.1 on 2020-03-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200308_1157'),
        ('cart', '0023_auto_20200322_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.ManyToManyField(to='index.Product'),
        ),
    ]
