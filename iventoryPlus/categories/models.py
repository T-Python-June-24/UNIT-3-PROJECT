from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=120,unique=True)
    def __str__(self) -> str:
        return self.name