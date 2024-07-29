from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='supplier_logos/', blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    expiry_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    suppliers = models.ManyToManyField(Supplier, related_name='products')

    def __str__(self):
        return self.name
