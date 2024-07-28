from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from products.models import Product
# Create your views here.



def home_view(request:HttpRequest):

    #get all products
    products = Product.objects.all().order_by("product_name")[0:3]

    return render(request, 'main/index.html', {"product" : products} )


def contact_view(request:HttpRequest):

    return render(request, 'main/contact.html' )



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response
