from django.db import models
from django.utils import timezone
from Supplier.models import Supplier
from Category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True)
    expiry_date = models.DateField()
    stock = models.IntegerField(default=0)  # Current inventory level
    minimum_stock = models.IntegerField(default=0)  # Minimum required stock level
    last_stock_update = models.DateTimeField(default=timezone.now)  # When the stock was last updated

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