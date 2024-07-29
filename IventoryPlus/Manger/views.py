from django.shortcuts import render
from django.http import HttpRequest
from product.models import Product
from Category.models import Category
from Supplier.models import Supplier
import plotly.express as px
import pandas
# Create your views here.


def Manger(request:HttpRequest):
    Quantity_product = Product.objects.filter(Quantity_Product__lt = 2).exclude(Quantity_Product=0)
    out_product = Product.objects.filter(Status_Product = 0)
    update_product = Product.objects.all().order_by('-Created_at')
    number_product = Product.objects.count()
    number_Supplier = Supplier.objects.count()
    number_Category = Category.objects.count()
    sold_out_product = Product.objects.filter(Quantity_Product=0).count()
    running_out_product = Product.objects.filter(Quantity_Product__lt=2).exclude(Quantity_Product=0).count()
    
    
    category = Category.objects.all()

    return render(request , 'pages/pages_manger.html' ,
                  {"Quantity_product":Quantity_product ,
                   "out_product":out_product , 
                   "update_product":update_product,
                   "number_product":number_product,
                   "number_supplier":number_Supplier,
                   "number_category":number_Category,
                   
                   })
    
def manger_product(request:HttpRequest):
    category = Category.objects.all()
    views_supplier = Supplier.objects.all()
    views_product = Product.objects.all().select_related('Category_product').prefetch_related('Supplier_product')
    return render(request , "pages/views_product.html" , {"views_product":views_product,"category":category , "views_supplier":views_supplier})

def manger_Category(request:HttpRequest):
    category = Category.objects.all()
    return render(request , "pages/views_category.html" , {"category":category})