from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Product
from datetime import datetime, timedelta

@receiver(post_save, sender=Product)
def check_inventory(sender, instance, **kwargs):
  # Low stock alert

  stock_quantity = int(instance.stock_quantity)

  low_stock = 10
  if stock_quantity <= low_stock:
    send_mail(
      'Low Stock Alert',
      f'The product {instance.name} is running low on stock (Stock: {instance.stock_quantity}).',
      'inventoryplus051@hotmail.com',
      ['boshraalija@gmail.com'],
      fail_silently=False,
    )

    # # Expiry date alert
    # today = datetime.now().date()
    # expiry_date = today + timedelta(days=30)
    # if instance.expiry_date and instance.expiry_date <= expiry_date:
    #     send_mail(
    #         'Expiry Date Alert',
    #         f'The product {instance.name} is nearing its expiry date (Expiry Date: {instance.expiry_date}).',
    #         'inventoryplus051@hotmail.com',
    #         ['boshraalija@gmail.com'],
    #         fail_silently=False,
    #     )
