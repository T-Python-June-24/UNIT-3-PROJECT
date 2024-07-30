from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product
from .forms import ProductForm
from Category.models import Category
from Supplier.models import Supplier
from django.contrib import messages  # Import messages
from .admin import ProductResource



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



def product_page(request):
    # Start with all products
    products = Product.objects.all()
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()

    # Check if a search was made
    searched = request.GET.get('searched', '')
    if searched:
        products = products.filter(name__icontains=searched)

    # Check for export action
    if 'export' in request.POST:
        dataset = ProductResource().export(products)
        response_data = dataset.csv
        content_type = 'text/csv'

        response = HttpResponse(response_data, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        return response
    #filter by category
    category=request.GET.get('category')
    if category:
        products = products.filter(category=category)
    #filter by supplier

    supplier_id = request.GET.get('supplier', '')
    if supplier_id:
        products = products.filter(suppliers__id=supplier_id)
    # Render the page normally if not exporting
    return render(request, "Product/products.html", {
        "categories": categories,
        "suppliers": suppliers,
        "products": products,
        "search_term": searched
    })