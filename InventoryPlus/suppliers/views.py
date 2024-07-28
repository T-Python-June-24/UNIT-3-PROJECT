from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Supplier
from .forms import SupplierForm

def add_supplier(request:HttpRequest):

    supplier_form = SupplierForm()

    if request.method == "POST":
        
        supplier_form = SupplierForm(request.POST, request.FILES)
        if supplier_form.is_valid():
            supplier_form.save()
            # return redirect('main:home_view')
        else:
            print("not valid form", supplier_form.errors)
    return render(request, "suppliers/add.html", {"supplier_form":supplier_form})


def all_suppliers(request:HttpRequest):


    return render(request, "suppliers/all_suppliers.html")

