from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Product
from .forms import ProductForms  
import os

def Add_product(request: HttpRequest):
    if request.method == 'POST':
        product_form = ProductForms(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('views_product')  
        else:
            print('Error:', product_form.errors)
    else:
        product_form = ProductForms()

    return render(request, 'index.html', {'form': product_form})
def views_product(request:HttpRequest):
    view_product = Product.objects.all().select_related('Category_product')
    return render(request , 'index.html' , {'product':view_product})
def update_product(request:HttpRequest , product_id):
    up_product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        up_product.Name_Product = request.POST['Name']
        up_product.Status_Product = request.POST['Status']
        up_product.Quantity_Product = request.POST['quantity']
        up_product.Price_Product = request.POST['price']
        up_product.Expiration_date = request.POST['expiration']
        up_product.Description_product = request.POST['description']
        up_product.Category_product = request.POST['category']
        up_product.Supplier_product = request.POST['supplier']
        if ['image'] in request.FILES: up_product.Images_Product = request.FILES['image']
        up_product.save()
        return redirect('Manger:manger_product')
    return render(request , 'product/update_product.html' )
def delete(request:HttpRequest , product_id):
    del_product = Product.objects.get(pk=product_id)
    if del_product.Images_Product:
        if os.path.isfile(del_product.Images_Product.path):
            os.remove(del_product.Images_Product.path)
    del_product.delete()
    return redirect('product:views_product')
def detail_product(request:HttpRequest , product_id):
    det_product = Product.objects.get(pk=product_id)
    return render(request , 'product/detail_product.html',{'product': det_product})