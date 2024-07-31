from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm
from .utils import send_low_stock_alert
import pandas as pd
import csv
from .forms import CSVUploadForm
from django.contrib import messages



def product_list(request):
    category = request.GET.get('category')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]
    return render(request, 'inventory/product_detail.html', {'product': product, 'related_products': related_products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('inventory:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:product_detail', pk=product.pk)  # Redirect to product detail after update
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('inventory:product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})




# category
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('inventory:category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('inventory:category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})



# supplier
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    products = supplier.products.all()
    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier, 'products': products})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventory:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/supplier_form.html', {'form': form})

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('inventory:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('inventory:supplier_list')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})




#search
def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
        suppliers = Supplier.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none()
        suppliers = Supplier.objects.none()
    return render(request, 'inventory/search_results.html', {
        'products': products,
        'suppliers': suppliers,
        'query': query,
        'product_count': products.count(),
        'supplier_count': suppliers.count(),
    })




#email notifications
def check_low_stock_products():
    low_stock_products = Product.objects.filter(stock__lt=10)
    for product in low_stock_products:
        send_low_stock_alert(product)

def inventory_report(request):
    products = Product.objects.all()
    low_stock_products = Product.objects.filter(stock__lt=10)

    check_low_stock_products()

    context = {
        'products': products,
        'low_stock_products': low_stock_products,
    }
    return render(request, 'analytics/inventory_report.html', context)



# CSV
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def import_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            try:
                data = pd.read_csv(csv_file)
                logger.debug(f'CSV Data: {data.head()}')

                # Check if required columns are present
                required_columns = ['name', 'category', 'price', 'stock', 'description', 'image']
                if not all(column in data.columns for column in required_columns):
                    messages.error(request, f'CSV file must contain the following columns: {", ".join(required_columns)}')
                    return redirect('inventory:import_csv')

                for index, row in data.iterrows():
                    category, _ = Category.objects.get_or_create(name=row['category'])
                    product, created = Product.objects.get_or_create(
                        name=row['name'],
                        defaults={
                            'category': category,
                            'price': row['price'],
                            'stock': row['stock'],
                            'description': row.get('description', ''),
                            'image': row.get('image', '')  # Assuming the CSV has URLs or paths to images
                        }
                    )
                    if not created:
                        product.category = category
                        product.price = row['price']
                        product.stock = row['stock']
                        product.description = row.get('description', '')
                        product.image = row.get('image', '')  # Update image if provided
                        product.save()
                messages.success(request, 'Products imported successfully.')
                return redirect('inventory:product_list')
            except Exception as e:
                logger.error(f'Error processing CSV file: {e}', exc_info=True)
                messages.error(request, f'Error processing CSV file: {e}')
                return redirect('inventory:import_csv')
    else:
        form = CSVUploadForm()
    return render(request, 'inventory/import_products.html', {'form': form})




def export_csv(request):
    products = Product.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    writer = pd.DataFrame(list(products.values('name', 'category__name', 'price', 'stock', 'description', 'image')))
    writer.columns = ['Name', 'Category', 'Price', 'Stock', 'Description', 'Image']
    writer.to_csv(path_or_buf=response, index=False)
    return response