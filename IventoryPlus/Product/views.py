from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product
from .forms import ProductForm
from Category.models import Category
from Supplier.models import Supplier
from django.contrib import messages  # Import messages


def add_product(request):
    products = Product.objects.all()
    categories=Category.objects.all()
    suppliers=Supplier.objects.all()
    if request.method == "POST":
        productForm = ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
            messages.success(request, 'Product added successfully!')
            return redirect("Product:Product_added_success")
        else:
            for field, errors in productForm.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return render(request, "Product/add_product.html",{"products" : products , "categories":categories,"suppliers":suppliers})

def Product_added_success(request):
    return render(request, "Product/added_success.html")
