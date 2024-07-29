from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product


# Create your views here.
def add(request: HttpRequest) -> HttpResponse:

    # new_product = Product()
    # new_product.save()
    return render(request, 'product/add.html')