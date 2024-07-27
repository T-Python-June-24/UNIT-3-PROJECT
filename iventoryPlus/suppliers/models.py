from django.db import models

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="images/",default="images/no-logo-png-6.png")
    email=models.EmailField()
    website=models.URLField()
    phone=models.CharField(max_length=10)
    country=models.CharField(max_length=100)
