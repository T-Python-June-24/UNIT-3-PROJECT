from django.shortcuts import render , redirect
from django.http import HttpRequest 
from product.models import Product
from Category.models import Category
from Supplier.models import Supplier

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
def manger_supplier(request:HttpRequest):
    supplier = Supplier.objects.all()
    return render(request , 'pages/views_supplier.html' ,{'supplier':supplier})
    
def search(request: HttpRequest):
    if request.method == 'GET':
        type_search = request.GET.get('type_search', '')
        if type_search == 'product':
            word_search = request.GET.get('search', '')
            products = Product.objects.filter(Name_Product__icontains=word_search)
            count_product = products.count()
            return render(request, 'pages/views_product.html', {
                'views_product': products,
                'count_product': count_product,
                'word_search': word_search
            })
        elif type_search == 'Category':
            word_search = request.GET.get('search', '')
            category = Category.objects.filter(name_Category__icontains=word_search)
            count_category = category.count()
            return render(request, 'pages/views_category.html', {
                'category': category,
                'count_category': count_category,
                'word_search': word_search
            })
        elif  type_search =="Supplier":
            word_search = request.GET.get('search', '')
            supplier = Supplier.objects.filter(name_Supplier__icontains=word_search)
            count_Supplier = supplier.count()
            return render(request, 'pages/views_Supplier.html', {
                'supplier': supplier,
                'count_Supplier': count_Supplier,
                'word_search': word_search
            })
            
    return redirect('Manger:manger_product')