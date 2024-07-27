from django.shortcuts import render
from django.http import HttpRequest
from .models import Product
from suppliers.models import Supplier
from categories.models import Category
# Create your views here.
def products_view(request:HttpRequest):
    my_range=range(50)
    return render(request,"products/product.html",{"range":my_range})
def add_product_view(request:HttpRequest)->render:
    product=Product.objects.all()
    suppliers=Supplier.objects.all()
    categories=Category.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        description=request.POST["description"]
        stock_level=request.POST['stock_level']
        expirment=None        
        price=request.POST["price"]
        category_id=request.POST["category"]
        category=Category.objects.get(id=category_id)
        
        new_product=Product(name=name,description=description,stock_level=stock_level,expirment=expirment,price=price,category=category)
        new_product.save()
        # new_product.supplier.set(request.POST.getlist("supplier"))

    return render(request,"products/add_product.html",{"suppliers":suppliers,"categories":categories,"product":product})