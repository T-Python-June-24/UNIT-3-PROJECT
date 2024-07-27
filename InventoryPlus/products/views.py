from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ProductForm
from .models import Product

# Create your views here.

def products_view(request: HttpRequest):
  products = Product.objects.all()
  return render(request, "products/products.html", {'products': products})



def add_product(request: HttpRequest):
  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("products:products_view")
  else:
    form = ProductForm

  return render(request, "products/add_product.html", {'form': form})




def edit_product_view(request: HttpRequest, product_id):
  product = Product.objects.get(pk=product_id)
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
      return redirect("products:products_view")
  else:
    form = ProductForm(instance=product)
  
  return render(request, "products/edit_product.html", {'form': form, 'product': product})



def delete_product_view(request: HttpRequest, product_id):
  product = Product.objects.get(pk=product_id)
  if request.method == "POST":
    product.delete()
    return redirect("products:products_view")
  return render(request, "delete_product.html", {'product': product})