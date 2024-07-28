from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Product
from suppliers.models import Supplier
from categories.models import Category
# Create your views here.
def products_view(request:HttpRequest):
    products=Product.objects.all()
    return render(request,"products/product.html",{"products":products})
def add_product_view(request:HttpRequest)->render:
    product=Product.objects.all()
    suppliers=Supplier.objects.all()
    categories=Category.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        description=request.POST["description"]
        stock_level=request.POST['stock_level']
        if request.POST["expirment_date"]=="":
            expirment=None
        else:
            expirment=request.POST["expirment_date"]
        
        price=request.POST["price"]
        category=Category.objects.get(pk=request.POST["category"])
        
        new_product=Product(name=name,description=description,stock_level=stock_level,expirment=expirment,price=price,category=category)
        new_product.save()
        new_product.supplier.set(request.POST.getlist("supplier"))

    return render(request,"products/add_product.html",{"suppliers":suppliers,"categories":categories,"product":product})

def update_product(request,product_id):

    product=Product.objects.get(pk=product_id)
    suppliers=Supplier.objects.all()
    categories=Category.objects.all()
    if request.method=="POST":
        product.name=request.POST['name']
        product.description=request.POST["description"]
        product.stock_level=request.POST['stock_level']
        if request.POST["expirment_date"]=="":
            product.expirment=None
        else:
            product.expirment=request.POST["expirment_date"]
        
        product.price=request.POST["price"]
        product.category=Category.objects.get(pk=request.POST["category"])
        product.save()
        product.supplier.set(request.POST.getlist("supplier"))
        return redirect("products:products_view")
    return render(request,"products/update_product.html",{"product":product,"suppliers":suppliers,"categories":categories})
    
def delete_product(requesr:HttpRequest,product_id):
    product=Product.objects.get(pk=product_id)
    product.delete()
    return redirect("products:products_view")
        
