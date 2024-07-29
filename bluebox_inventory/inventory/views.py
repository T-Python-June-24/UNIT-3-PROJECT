from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm
from django.http import HttpResponse
import pandas as pd

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

# Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('category_list')
    return render(request, 'category/category_confirm_delete.html', {'category': category})

# Supplier Views
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier})

def supplier_create(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/supplier_form.html', {'form': form})

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})

# Analysis and Export Views
def analysis(request):
    products = Product.objects.all()
    suppliers = Supplier.objects.all()
    categories = Category.objects.all()
    
    # Data for chart.js
    product_data = {
        'labels': [product.name for product in products],
        'data': [product.stock_quantity for product in products]
    }
    
    context = {
        'product_data': product_data,
        'products': products,
        'suppliers': suppliers,
        'categories': categories
    }
    
    return render(request, 'inventory/analysis.html', context)

def export_csv(request):
    products = Product.objects.all()
    df = pd.DataFrame(list(products.values()))
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    df.to_csv(path_or_buf=response, index=False)
    
    return response
