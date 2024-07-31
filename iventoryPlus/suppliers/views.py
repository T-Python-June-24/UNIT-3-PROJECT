from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Supplier
from products.models import Product
import time
import math
import pandas as pd
from django.http import HttpResponse
# Create your views here.
def all_suppliers(request:HttpRequest):
    suppliers=Supplier.objects.all()
    totalProducts=Product.objects.all().count()
    for index, supplier in enumerate(suppliers):
        suppliers[index].percentage = math.floor((supplier.product_set.all().count()/totalProducts)*100)
    

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
        return redirect(request.GET.get("next","/"))
    return render(request,"suppliers/update_supplier.html",{"supplier":supplier})

def supplier_detailes(request:HttpRequest,supplier_id):
    supplier=Supplier.objects.get(pk=supplier_id)
    totalProducts=Product.objects.all().count()
    supplier_percentage=math.floor((supplier.product_set.count()/totalProducts)*100)
    products=Product.objects.filter(supplier=supplier)
    return render (request,"suppliers/supplier_detailes.html",{"supplier":supplier,"supplier_percentage":supplier_percentage,"products":products})
def export_suppliers(request):
    # Get all suppliers
    suppliers = Supplier.objects.all()

    # Create a list of dictionaries from the queryset
    data = []
    for supplier in suppliers:
        data.append({
            'name': supplier.name,
            'email': supplier.email,
            'website': supplier.website,
            'phone': supplier.phone,
            'country': supplier.country,
            'added': supplier.added,
        })

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Convert the DataFrame to a CSV string
    csv_data = df.to_csv(index=False)

    # Create an HTTP response with the CSV data
    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=suppliers.csv'

    return response