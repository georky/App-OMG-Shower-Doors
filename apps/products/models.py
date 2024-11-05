# productos/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', blank=True)  # Para una sola imagen
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    sku = models.CharField(max_length=50)
    tags = models.CharField(max_length=100)  # Podrías usar un ManyToManyField para etiquetas

    def __str__(self):
        return self.name

