from django.shortcuts import render, get_object_or_404
from .models import Notification
from .utils import send_notification_email

# Create your views here.

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def notify_low_stock(product):
    subject = f'Low Stock Alert for {product.name}'
    message = f'The stock for {product.name} is low. Current stock level: {product.stock}'
    recipient_list = ['manager@example.com']
    send_notification_email(subject, message, recipient_list)

