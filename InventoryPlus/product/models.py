from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # supplier_ID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    expiry_date = models.DateField()
    reorder_level = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
