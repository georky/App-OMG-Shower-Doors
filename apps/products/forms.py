# productos/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'weight', 'description', 'category', 'size', 'image', 'price', 'currency', 'sku', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }
