from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Supplier
from .forms import SupplierForm
from django.contrib import messages  # Import messages


def add_supplier(request):
    suppliers = Supplier.objects.all()
    if request.method == "POST":
        supplierForm = SupplierForm(request.POST, request.FILES)
        if supplierForm.is_valid():
            supplierForm.save()
            messages.success(request, 'Supplier added successfully!')
            return redirect("Supplier:added_success")
        else:
            for field, errors in supplierForm.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return render(request, "Supplier/add_supplier.html",{"suppliers" : suppliers})

def added_success(request):
    return render(request, "Supplier/added_success.html")

def supplier_page(request:HttpRequest):

    suppliers = Supplier.objects.all()

    return render(request, "Supplier/suppliers.html", {"suppliers" : suppliers})

def supplier_detail(request,supplier_id:int):

    supplier = Supplier.objects.get(pk=supplier_id)
    return render(request, "Supplier/supplier_detail.html",{"supplier":supplier})

def supplier_update(request, supplier_id: int):
    supplier = Supplier.objects.get(pk=supplier_id)
    if request.method == "POST":
        supplierForm = SupplierForm(request.POST, request.FILES, instance=supplier)
        if supplierForm.is_valid():
            supplierForm.save()
            return redirect('Supplier:supplier_detail', supplier_id=supplier.id)

    return render(request, 'Supplier/supplier_detail.html', {'supplierForm': supplierForm, 'supplier': supplier})

def delete_supplier(request:HttpRequest,supplier_id:int):
    supplier = Supplier.objects.get(pk=supplier_id)
    supplier.delete()
    return redirect('Supplier:supplier_page')
