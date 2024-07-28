from django.db import models
from Supplier.models import Supplier
from Category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    suppliers = models.ManyToManyField(Supplier)
    expiry_date = models.DateField()
    stock = models.IntegerField(default=0)  # Current inventory level
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    minimum_stock = models.IntegerField(default=0)  # Minimum required stock level

    def stock_status(self):
        """Determines the stock status based on current inventory levels."""
        if self.stock <= 0:
            return 'Out of Stock'
        elif self.stock <= self.minimum_stock:
            return 'Low Stock'
        else:
            return 'In Stock'

    def __str__(self):
        return self.name