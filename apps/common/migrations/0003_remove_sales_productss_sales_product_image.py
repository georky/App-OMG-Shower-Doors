# Generated by Django 4.2.9 on 2024-11-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_sales_productss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='Productss',
        ),
        migrations.AddField(
            model_name='sales',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
