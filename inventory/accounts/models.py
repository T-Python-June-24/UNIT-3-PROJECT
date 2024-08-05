from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="images/avatars/", default="images/avatars/avatar.webp")
    twitch_link = models.URLField(blank=True)


    def __str__(self) -> str:
        return f"Profile {self.user.username}"
    



class Bookmark(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)





