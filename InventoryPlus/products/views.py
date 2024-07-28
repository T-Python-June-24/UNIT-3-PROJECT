from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .forms import ProductForm
from .models import Category,Supplier,Product

# Create your views here.


def add_product_view(request:HttpRequest):

    product_form = ProductForm()

    categories = Category.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('main:home_view')
        else:
            print("not valid form", product_form.errors)
        # category = Category.objects.get(id=request.POST["category"])
        # new_product = Product(product_name=request.POST["product_name"], description=request.POST["description"], category=category, stock_level=request.POST["stock_level"], expiry_date=request.POST["expiry_date"], image=request.FILES["image"])
        # new_product.save()
        # new_product.suppliers.set(request.POST.getlist("suppliers"))
        # return redirect('main:home_view')
    
    return render(request, "products/add.html", {"product_form":product_form, "categories":categories, "suppliers": suppliers})

def all_products_view(request:HttpRequest, category_name):
    # products = Product.objects.filter(stock_level__gte=3).order_by("-expiry_date")
    # products = Product.objects.filter(stock_level__gte=3).exclude(product_name__contains="iphon11").order_by("-expiry_date")
    
    # if  Category.objects.filter(supplier_name=supplier_name).exists():
    #     products = Product.objects.filter(suppliers__supplier_name__in=[supplier_name]).order_by("-expiry_date")
    # elif supplier_name == "all":
    #     products = Product.objects.all().order_by("-expiry_date")
    # else:
    #     products = []

    
    if category_name == "all":
        products = Product.objects.all().order_by("-expiry_date")
    else:
        products = Product.objects.filter(category__name = category_name).order_by("-expiry_date")
        # products = Product.objects.filter(suppliers__supplier_name__in=[supplier_name]).order_by("-expiry_date")


    return render(request, "products/all_products.html", {"products":products, "category_name":category_name})




def search_products_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 2:
        products = Product.objects.filter(product_name__contains=request.GET["search"])

        if "order_by" in request.GET and request.GET["order_by"] == "stock_level":
            products = products.order_by("-stock_level")
        elif "order_by" in request.GET and request.GET["order_by"] == "expiry_date":
            products = products.order_by("-expiry_date")
    else:
        products = []


    return render(request, "products/search_products.html", {"products" : products})
