from django.shortcuts import render
from inventory.models import Product, Supplier

def inventory_report(request):
    products = Product.objects.all()
    return render(request, 'analytics/inventory_report.html', {'products': products})

def supplier_report(request):
    suppliers = Supplier.objects.all()
    return render(request, 'analytics/supplier_report.html', {'suppliers': suppliers})
