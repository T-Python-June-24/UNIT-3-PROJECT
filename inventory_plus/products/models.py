from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    suppliers = models.ManyToManyField('suppliers.Supplier')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
