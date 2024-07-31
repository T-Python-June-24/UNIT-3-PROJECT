from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Product, Review, Category
from .forms import ProductForm
from suppliers.models import Supplier

# add your views here.

def add_product_view(request:HttpRequest):

    product_form = ProductForm()
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect("main:home")
        else:
            print("not valid form", product_form.errors)

    return render(request, "products/add.html", {"product_form":product_form, "categories":categories, "suppliers": suppliers})


def product_detail_view(request:HttpRequest, product_id:int):

    product = Product.objects.get(pk=product_id)
    reviews = Review.objects.filter(product=product)

    return render(request, 'products/product_detail.html', {"product" : product, "reviews":reviews})


def product_update_view(request:HttpRequest, product_id:int):

    product = Product.objects.get(pk=product_id)
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        #using ProductForm for updating
        product_form = ProductForm(instance=product, data=request.POST, files=request.FILES)
        if product_form.is_valid():
            product_form.save()
        else:
            print(product_form.errors)
        ##basic update
        # product.title = request.POST["title"]
        # product.description = request.POST["description"]
        # product.production_date = request.POST["production_date"]
        # product.supplier = request.POST["supplier"]
        # product.rating = request.POST["rating"]
        # if "poster" in request.FILES: product.poster = request.FILES["poster"]
        # product.save()

        return redirect("products:product_detail_view", product_id=product.id)

    return render(request, "products/product_update.html", {"product":product, "categories" : categories, "suppliers": suppliers})


def product_delete_view(request:HttpRequest, product_id:int):

    product = Product.objects.get(pk=product_id)
    product.delete()

    return redirect("main:home")


def all_products_view(request:HttpRequest, category_name):
    #products = Product.objects.filter(rating__gte=3).order_by("-production_date")
    #products = Product.objects.filter(rating__gte=3).exclude(title__contains="Legends").order_by("-production_date")
    
    # if  Category.objects.filter(name=category_name).exists():
    #     products = Product.objects.filter(categories__name__in=[category_name]).order_by("-production_date")
    # elif category_name == "all":
    #     products = Product.objects.all().order_by("-production_date")
    # else:
    #     products = []

    
    if category_name == "all":
        products = Product.objects.all().order_by("-production_date")
    else:
        products = Product.objects.filter(categories__name__in=[category_name]).order_by("-production_date")


    return render(request, "products/all_products.html", {"products":products, "category_name":category_name})


def search_products_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 3:
        products = Product.objects.filter(title__contains=request.GET["search"])

        if "order_by" in request.GET and request.GET["order_by"] == "rating":
            products = products.order_by("-rating")
        elif "order_by" in request.GET and request.GET["order_by"] == "production_date":
            products = products.order_by("-production_date")
    else:
        products = []


    return render(request, "products/search_products.html", {"products" : products})


def add_review_view(request:HttpRequest, product_id):

    if request.method == "POST":
        product_object = Product.objects.get(pk=product_id)
        new_review = Review(product=product_object,name=request.POST["name"],comment=request.POST["comment"],rating=request.POST["rating"])
        new_review.save()

    return redirect("products:product_detail_view", product_id=product_id)