from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Product
from .forms import ProductForms  

def views_product(request: HttpRequest):
    if request.method == 'POST':
        product_form = ProductForms(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('success')  
        else:
            print('Error:', product_form.errors)
    else:
        product_form = ProductForms()

    return render(request, 'index.html', {'form': product_form})
