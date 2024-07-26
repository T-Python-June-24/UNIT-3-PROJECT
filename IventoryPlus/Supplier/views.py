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