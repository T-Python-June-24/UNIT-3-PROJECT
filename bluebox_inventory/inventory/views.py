from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm, SignUpForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
import pandas as pd
import csv
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
# inventory/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Supplier, ContactMessage
from .forms import ProductForm, CategoryForm, SupplierForm, ContactForm

# Dashboard view

# Product views
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

# Category views
@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'inventory/category_form.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'inventory/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'inventory/category_confirm_delete.html', {'category': category})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'inventory/category_list.html', {'categories': categories})

# Supplier views
@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'inventory/supplier_form.html', {'form': form})

@login_required
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/supplier_form.html', {'form': form})

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'inventory/supplier_confirm_delete.html', {'supplier': supplier})

@login_required
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'inventory/supplier_detail.html', {'supplier': supplier})

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers})

# Contact views
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'inventory/contact.html', {'form': form})

@login_required
def contact_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'inventory/contact_messages.html', {'messages': messages})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after signup
            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard')  # Redirect to a dashboard or home page
    else:
        form = UserCreationForm()
        messages.success(request, 'There is a problem.')
    return render(request, 'inventory/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard')  # Redirect to a dashboard or home page
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout
#######################################
def dashboard(request):
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()

    # Stock data for chart
    stock_data = {
        'labels': [product.name for product in Product.objects.all()],
        'data': [product.stock_quantity for product in Product.objects.all()]
    }

    # Recent activities (for example purposes, replace with actual activities)
    recent_activities = [
        "Product A was added",
        "Product B stock updated",
        "Supplier X added a new product"
    ]

    # Alerts for low stock and expiring products
    low_stock_products = Product.objects.filter(stock_quantity__lte=5)
    expiring_soon_products = Product.objects.filter(expiry_date__lte=timezone.now().date() + timedelta(days=5))

    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_suppliers': total_suppliers,
        'stock_data': stock_data,
        'recent_activities': recent_activities,
        'low_stock_products': low_stock_products,
        'expiring_soon_products': expiring_soon_products
    }

    return render(request, 'inventory/dashboard.html', context)


def export_csv(request, data_type):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{data_type}_data.csv"'

    writer = csv.writer(response)

    if data_type == 'products':
        writer.writerow(['Product Name', 'Category', 'Supplier', 'Price', 'Stock Quantity'])
        products = Product.objects.all()
        for product in products:
            writer.writerow([product.name, product.category.name, product.supplier.name, product.price, product.stock_quantity])
    
    elif data_type == 'suppliers':
        writer.writerow(['Supplier Name', 'Email', 'Phone', 'Address', 'Website'])
        suppliers = Supplier.objects.all()
        for supplier in suppliers:
            writer.writerow([supplier.name, supplier.email, supplier.phone, supplier.address, supplier.website])
    
    elif data_type == 'categories':
        writer.writerow(['Category Name'])
        categories = Category.objects.all()
        for category in categories:
            writer.writerow([category.name])
    
    return response

############


def analysis(request):
    # Product stock data for chart
    product_stock_data = {
        'labels': [product.name for product in Product.objects.all()],
        'data': [product.stock_quantity for product in Product.objects.all()]
    }

    # Supplier stock data for chart
    supplier_stock_data = {
        'labels': [supplier.name for supplier in Supplier.objects.all()],
        'data': [sum(product.stock_quantity for product in supplier.product_set.all()) for supplier in Supplier.objects.all()]
    }

    # Category stock data for chart
    category_stock_data = {
        'labels': [category.name for category in Category.objects.all()],
        'data': [sum(product.stock_quantity for product in category.product_set.all()) for category in Category.objects.all()]
    }

    context = {
        'product_stock_data': product_stock_data,
        'supplier_stock_data': supplier_stock_data,
        'category_stock_data': category_stock_data
    }

    return render(request, 'inventory/analysis.html', context)
