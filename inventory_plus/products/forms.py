from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'suppliers', 'description', 'price', 'stock_quantity', 'expiry_date']
