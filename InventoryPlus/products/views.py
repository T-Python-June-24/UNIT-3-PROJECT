from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Product, Category
from django.db.models import Q

# Create your views here.

def products_view(request: HttpRequest):
  products = Product.objects.all()
  return render(request, "products/products.html", {'products': products})



def add_product(request: HttpRequest):
  Categories = Category.objects.all()

  if request.method == 'POST':
    name = request.POST.get('name')
    category_id = request.POST['category']
    category = Category.objects.get(pk=category_id)
    image = request.FILES.get('image')
    description = request.POST.get('description')
    price = request.POST.get('price')
    stock_quantity = request.POST.get('stock_quantity')

    product = Product(name=name, category=category, image=image, description=description, price=price, stock_quantity=stock_quantity)
    product.save()

    return redirect("products:products_view")
  
  return render(request, "products/add_product.html")




def edit_product_view(request: HttpRequest, product_id):
  product = Product.objects.get(pk=product_id)
  
  if request.method == 'POST':
    product.name = request.POST.get('name')
    product.image = request.FILES.get('image', product.image)
    product.description = request.POST.get('description')
    product.price = request.POST.get('price')
    product.stock_quantity = request.POST.get('stock_quantity')
    product.save()
    return redirect("products:edit_product_view", product_id=product_id)
  
  return render(request, "products/edit_product.html", {'product': product})



def delete_product_view(request: HttpRequest, product_id):
  product = Product.objects.get(pk=product_id)
  product.delete()
  return redirect("products:products_view")




def product_detail_view(request: HttpRequest, product_id):
  product = Product.objects.get(pk = product_id)
  return render(request, "products/product_details.html", {'product': product})



def product_search_view(request: HttpRequest):
  query = request.GET.get('q')
  if query:
    products = Product.objects.filter(
      Q(name__icontains=query) |
      Q(description__icontains=query)
    )
  else:
    products = Product.objects.all()
  return render(request, "products/products.html", {'products': products})


def categories_view(request: HttpRequest):
  categories = Category.objects.all()
  return render(request, 'products/category.html', {'categories': categories})


def add_category_view(request: HttpRequest):
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')

    category = Category(name=name, description=description)
    category.save()

    return redirect("products:categories_view")
  
  return render(request, 'products/add_category.html')


def edit_category_view(request: HttpRequest, category_id):
  category = Category.objects.get(pk=category_id)

  if request.method == 'POST':
    category.name = request.POST.get('name')
    category.description = request.POST.get('description')
    category.save()
    return redirect('products:categories_view')
  
  return render(request, 'products/edit_category.html', {'category': category})



def delete_category_view(request: HttpRequest, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('products:categories_view')

