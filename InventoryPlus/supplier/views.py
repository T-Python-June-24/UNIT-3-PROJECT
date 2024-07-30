from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Supplier
from .forms import SupplierForm


# Create your views here.
def add_view(request: HttpRequest) -> HttpResponse:
    supplier_form = SupplierForm()
    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            supplier_form.save()
            return redirect('main:index_view')
    else:
        print("not valid form", supplier_form.errors)
    return render(request, 'supplier/add.html', {'supplier_form': supplier_form})


def edit_view(request: HttpRequest, supplier_id: int) -> HttpResponse:
    supplier = Supplier.objects.get(id=supplier_id)
    # supplier_form = SupplierForm(instance=supplier)
    return render(request, 'supplier/edit.html', {'supplier': supplier})


def all_view(request: HttpRequest) -> HttpResponse:
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/all.html', {'suppliers': suppliers})


def detail_view(request: HttpRequest, supplier_id: int) -> HttpResponse:
    supplier = Supplier.objects.get(id=supplier_id)
    return render(request, 'supplier/detail.html', {'supplier': supplier})


def delete_view(request: HttpRequest, supplier_id: int) -> HttpResponse:
    supplier = Supplier.objects.get(id=supplier_id)
    supplier.delete()
    return redirect('main:index_view')


def search_view(request: HttpRequest) -> HttpResponse:
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        suppliers = Supplier.objects.filter(title__contains=request.GET["search"])
    else:
        suppliers = []
    return render(request, 'supplier/search.html', {'suppliers': suppliers})
