from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from products.models import Product
from suppliers.models import Supplier


def home(request:HttpRequest):

    #get all products
    products = Product.objects.all().order_by("-production_date")[0:3]
    suppliers = Supplier.objects.all().order_by("pk")[0:3]

    return render(request, 'main/home.html', {"products" : products} )


def contact(request:HttpRequest):

    return render(request, 'main/contact.html' )

def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response