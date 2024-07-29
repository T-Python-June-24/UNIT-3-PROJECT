from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product
from .forms import ProductForm
from Category.models import Category
from Supplier.models import Supplier
from django.contrib import messages  # Import messages
from django.core.mail import send_mail

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

def product_page(request):
    # Start with all products
    products = Product.objects.all()
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()

    # Check if a search was made
    if 'searched' in request.GET:
        searched = request.GET['searched']
        if searched:

            products = products.filter(name__icontains=searched)

    return render(request, "Product/products.html", {
        "categories": categories,
        "suppliers": suppliers,
        "products": products,
        "search_term": searched if 'searched' in request.GET else ""
    })
def product_detail(request,product_id:int):

    product = Product.objects.get(pk=product_id)
    suppliers = Supplier.objects.all()
    categories = Category.objects.all()
    return render(request, 'Product/product_detail.html', {"product" : product ,"suppliers":suppliers , 'categories':categories})


def product_update(request, product_id: int):
    product = Product.objects.get(pk=product_id)
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        productForm = ProductForm(request.POST, request.FILES, instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect("Product:product_page")
        else:
            print(productForm.errors)

    return render(request, 'Product/product_detail.html', {
        'product': product,
        'categories': categories,
        'suppliers': suppliers
    })

def delete_product(request:HttpRequest,product_id:int):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('Product:product_page')


def search_product(request:HttpRequest):
    return redirect('Product:product_page')


