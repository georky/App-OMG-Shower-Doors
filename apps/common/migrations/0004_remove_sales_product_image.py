# Generated by Django 4.2.9 on 2024-11-03 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_sales_productss_sales_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='product_image',
        ),
    ]
