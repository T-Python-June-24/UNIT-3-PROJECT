from django.db import models
from category.models import Category
from supplier.models import Supplier

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

def __str__(self):
        return self.name