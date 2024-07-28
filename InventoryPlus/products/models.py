from django.db import models
from suppliers.models import Supplier
from categories.models import Category

# - As an Inventory Manager, I want to view a list of all inventory supplied by a supplier so that I can track how much business we do with the supplier.

class Product(models.Model):
    productName = models.CharField(max_length=128)
    productDescription = models.TextField()
    productImage = models.ImageField(upload_to='images/')
    productPrice = models.FloatField() # يحدده البائع 
    productionDate = models.DateField() 
    expirationDate = models.DateField()
    productStock = models.IntegerField() #بالبدايه راح تتعبى القيمه من السبلايرز في صفحة تسجيل المنتج 
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # المفترض تكون سيلكت اوبشن ويختار منها المدير 
    productSupplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplied_products') # should be select options 
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.productName

