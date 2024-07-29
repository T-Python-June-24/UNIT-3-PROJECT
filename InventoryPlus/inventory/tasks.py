from django.core.mail import send_mail
from django.utils import timezone
from .models import Product
from datetime import timedelta



def send_low_stock_alerts():
    low_stock_products = Product.objects.filter(stock__lt=10)
    if low_stock_products.exists():
        product_list = "\n".join([f"{p.name}: {p.stock}" for p in low_stock_products])
        send_mail(
            'Low Stock Alert',
            f'The following products are low in stock:\n{product_list}',
            'noreply@inventoryplus.com',
            ['manager@example.com']
        )



def send_expiry_alerts():
    expiry_date = timezone.now() + timedelta(days=30)
    expiring_products = Product.objects.filter(expiry_date__lte=expiry_date)
    if expiring_products.exists():
        product_list = "\n".join([f"{p.name}: {p.expiry_date}" for p in expiring_products])
        send_mail(
            'Expiry Date Alert',
            f'The following products are nearing expiry:\n{product_list}',
            'noreply@inventoryplus.com',
            ['manager@example.com']
        )
