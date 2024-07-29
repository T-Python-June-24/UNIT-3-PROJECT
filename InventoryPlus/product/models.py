from django.db import models
from category.models import Category
from supplier.models import Supplier


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    suppliers = models.ManyToManyField(Supplier, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    expiry_date = models.DateField(null=True)
    reorder_level = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
