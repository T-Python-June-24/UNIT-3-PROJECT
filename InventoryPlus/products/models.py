from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=512)
  description = models.TextField()

class Product(models.Model):
  name = models.CharField(max_length=512)
  image = models.ImageField(upload_to="images/")
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock_quantity = models.IntegerField()
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

