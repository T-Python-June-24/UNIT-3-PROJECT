from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()
    logo = models.ImageField(upload_to='suppliers/logos/', null=True, blank=True)

    def __str__(self):
        return self.name
