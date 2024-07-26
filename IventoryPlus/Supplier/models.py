from django.db import models

# Create your models here.
class Supplier(models.Model):

    name = models.CharField(max_length=1024)
    email = models.EmailField()
    logo = models.ImageField(upload_to="images/", default="images/default.jpg")
    phone_number = models.CharField(max_length=12)
    website= models.URLField(max_length=200)
    def __str__(self) -> str:
        return f"{self.name}"