from django.db import models

# Create your models here.



class Category(models.Model):
    name_Category = models.CharField(max_length=255)
    
    
    