from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Supplier
import time
# Create your views here.
def all_suppliers(request:HttpRequest):
    suppliers=Supplier.objects.all()
    #print(suppliers[0].product_set.all())

    for index, supplier in enumerate(suppliers):
        suppliers[index].percentage = 9

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

def delete_supplier(request:HttpRequest,supplier_id):
    supplier=Supplier.objects.get(pk=supplier_id)
    supplier.delete()
    return redirect("suppliers:all_suppliers")
def update_supplier(request:HttpRequest,supplier_id):
    supplier=Supplier.objects.get(pk=supplier_id)
    if request.method=="POST":
        supplier.name=request.POST["name"]
        supplier.email=request.POST["email"]
        supplier.website=request.POST["website_url"]
        supplier.phone=request.POST["phone_number"]
        supplier.country=request.POST["country"]
        if "logo" in request.FILES: supplier.logo=request.FILES['logo']
        supplier.save()
        return redirect("suppliers:all_suppliers")
    return render(request,"suppliers/update_supplier.html",{"supplier":supplier})