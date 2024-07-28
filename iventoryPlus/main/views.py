from django.shortcuts import render,redirect
from django.http import HttpRequest
from products.models import Product
from categories.models import Category
from suppliers.models import Supplier
from django.utils.timezone import now

# Create your views here.
def home_view(request:HttpRequest):
    products=Product.objects.all()
    products_count=products.count()
    suppliers_count=Supplier.objects.all().count()
    # added_today_suppliers=Supplier.objects.filter(added=now().date())
    total_values=0
    for product in products:
        total_values+=product.price

    return render(request,"main/index.html",{"total_value":total_values,"products_count":products_count,"suppliers_count":suppliers_count})



def search_view(request: HttpRequest):
    search_words = request.GET.get("search", "")
    filter_type = request.GET.get("filter", "all")

    products_result = []
    categories_result = []
    suppliers_result = []

    if search_words:
        if filter_type == "all":
            products_result = Product.objects.filter(name__icontains=search_words)
            categories_result = Category.objects.filter(name__icontains=search_words)
            suppliers_result = Supplier.objects.filter(name__icontains=search_words)
        elif filter_type == "product":
            products_result = Product.objects.filter(name__icontains=search_words)
        elif filter_type == "supplier":
            suppliers_result = Supplier.objects.filter(name__icontains=search_words)
        elif filter_type == "category":
            categories_result = Category.objects.filter(name__icontains=search_words)

    context = {
        "products": products_result,
        "categories": categories_result,
        "suppliers": suppliers_result,
        "search": filter_type,
    }

    return render(request, "main/search.html", context)
