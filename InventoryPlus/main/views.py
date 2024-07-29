from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from products.models import Product,Supplier,Category
from datetime import datetime,timedelta
# Create your views here.



def home_view(request:HttpRequest):

    products = Product.objects.all().order_by("product_name")
    suppliers = Supplier.objects.all().order_by("supplier_name")
    categories = Category.objects.all().order_by("name")

    # Calculate the date 10 days from today
    ten_days_from_today = datetime.now().date()+ timedelta(days=10)
    # Filter products with expiry_date less than or equal to 10 days from today
    ex_products = Product.objects.filter(expiry_date__lte=ten_days_from_today).order_by('product_name')

    return render(request, 'main/index.html', {"products" : products,"suppliers": suppliers, 'categories': categories, 'ex_products':ex_products})


def contact_view(request:HttpRequest):

    return render(request, 'main/contact.html' )



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response
