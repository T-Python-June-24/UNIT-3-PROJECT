from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Category
from products.models import Product
# Create your views here.
def all_categories(request:HttpRequest):
    categories=Category.objects.all()
    return render(request,"categories/category.html",{"categories":categories})

def add_category(request:HttpRequest):
    if request.method=="POST":
        name=request.POST["name"]
        new_category=Category(name=name)
        new_category.save()
    return render(request,"categories/add_category.html")

def delete_category(request,category_id):
    category=Category.objects.get(pk=category_id)
    product_update=Product.objects.filter(category=category)
    product_update.update(category=None)
    category.delete()
    return redirect("categories:all_categories")
def update_category(request:HttpRequest,category_id):
    category=Category.objects.get(pk=category_id)
    if request.method=="POST":
        category.name=request.POST["name"]
        category.save()
        return redirect("categories:all_categories")
    return render(request,"categories/update_category.html",{"category":category})
    
