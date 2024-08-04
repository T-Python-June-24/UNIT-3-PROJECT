from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Supplier
from Product.models import Product
from .forms import SupplierForm
from django.contrib import messages  # Import messages
from .admin import SupplierResource
from django.db.models import Count
from django.core.paginator import Paginator
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
    return render(request, "Supplier/add_supplier.html",{"suppliers" : suppliers })

def added_success(request):
    return render(request, "Supplier/added_success.html")


def supplier_page(request:HttpRequest):

    suppliers = Supplier.objects.all().annotate(products_count=Count("product"))

    if 'searched' in request.GET:
        searched = request.GET['searched']
        if searched:

            suppliers = suppliers.filter(name__icontains=searched)
    if 'export' in request.POST:
        dataset = SupplierResource().export(suppliers)
        response_data = dataset.csv
        content_type = 'text/csv'

        response = HttpResponse(response_data, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="suppliers.csv"'
        return response
    
    page_number=request.GET.get('page',1)
    paginator=Paginator(suppliers,2)
    suppliers=paginator.get_page(page_number)

    return render(request, "Supplier/suppliers.html", {"suppliers" : suppliers,
 "search_term": searched if 'searched' in request.GET else ""
})




def supplier_detail(request,supplier_id:int):

    supplier = Supplier.objects.get(pk=supplier_id)
    products=supplier.product_set.all()
    return render(request, "Supplier/supplier_detail.html",{"supplier":supplier , "products":products})

def supplier_update(request, supplier_id: int):
    supplier = Supplier.objects.get(pk=supplier_id)
    if request.method == "POST":
        supplierForm = SupplierForm(request.POST, request.FILES, instance=supplier)
        if supplierForm.is_valid():
            supplierForm.save()
            messages.success(request, 'Supplier updated successfully!')
            return redirect('Supplier:supplier_page')
        else:
            for field, errors in supplierForm.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return render(request, 'Supplier/supplier_detail.html', {'supplierForm': supplierForm, 'supplier': supplier})
def delete_supplier(request:HttpRequest,supplier_id:int):
    supplier = Supplier.objects.get(pk=supplier_id)
    if supplier.delete():
            messages.success(request, 'Supplier deleted successfully!')
            return redirect('Supplier:supplier_page')
    else:
        for field, errors in supplier.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")    
    return redirect('Supplier:supplier_page')
