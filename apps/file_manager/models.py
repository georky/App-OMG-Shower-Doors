from django.db import models

# Create your models here.


class FileInfo(models.Model):

 Product = models.TextField(blank=True, null=True)
 BuyerEmail = models.EmailField(blank=True, null=True)
 PurchaseDate = models.DateField(blank=True, null=True)
 Country = models.TextField(blank=True, null=True)
 Price = models.FloatField(blank=True, null=True)
 #Refunded = models.CharField(max_length=20, choices=RefundedChoices.choices, default=RefundedChoices.NO)
 #Currency = models.CharField(max_length=10, choices=CurrencyChoices.choices, default=CurrencyChoices.USD)
 Quantity = models.IntegerField(blank=True, null=True)
 path = models.URLField()
 info = models.CharField(max_length=255)

def __str__(self):
     return self.path