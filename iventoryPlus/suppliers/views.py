from django.shortcuts import render
from django.http import HttpRequest
from .models import Supplier
# Create your views here.
def all_suppliers(request:HttpRequest):
    suppliers=Supplier.objects.all()
    return render(request,"suppliers/supplier.html",{"suppliers":suppliers})

def add_supplier(request:HttpRequest):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        website_url=request.POST["website_url"]
        phone_number=request.POST["phone_number"]
        country=request.POST["country"]
        logo=request.FILES['logo']
        spplier=Supplier(name=name,email=email,website=website_url,phone=phone_number,country=country,logo=logo)
        spplier.save()
        
    return render(request,"suppliers/add_supplier.html")
