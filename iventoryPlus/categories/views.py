from django.shortcuts import render
from django.http import HttpRequest
from .models import Category
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
