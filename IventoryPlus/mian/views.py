from django.shortcuts import render
from django.http import HttpRequest
from product.models import Product
# Create your views here.

def home(request:HttpRequest):
    views_product = Product.objects.all()
    
    return render(request , 'pages/index.html' , {'views_product':views_product})