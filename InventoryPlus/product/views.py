from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product
from category.models import Category
from supplier.models import Supplier
from .forms import ProductForm


# Create your views here.
def add_view(request: HttpRequest) -> HttpResponse:
    product_form = ProductForm()
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('product:all_view')
    else:
        print("not valid form", product_form.errors)
    return render(request, 'product/add.html',
                  {'product_form': product_form, 'categories': categories, 'suppliers': suppliers})


def edit_view(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        product_form = ProductForm(instance=product, data=request.POST, files=request.FILES)
        if product_form.is_valid():
            product_form.save()
        else:
            print("not valid form", product_form.errors)
        return redirect('product:detail_view', product_id=product_id)

    return render(request, 'product/edit.html', {'product': product, 'categories': categories, 'suppliers': suppliers})


def all_view(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(request, 'product/all.html', {'products': products})


def detail_view(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    return render(request, 'product/detail.html', {'product': product})


def delete_view(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('product:all_view')


def search_view(request: HttpRequest) -> HttpResponse:
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        products = Product.objects.filter(name__contains=request.GET["search"])
    else:
        products = []
    return render(request, 'product/search.html', {'products': products})
