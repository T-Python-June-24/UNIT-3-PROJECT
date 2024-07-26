from django.shortcuts import render , redirect
from django.http import HttpRequest
from .models import Supplier
from .forms import SupplierForms
import os
# Create your views here.


def Add_Supplier(request:HttpRequest):
    if request.method == 'POST':
        supplier_form = SupplierForms(request.POST, request.FILES)
        if supplier_form.is_valid():
            supplier_form.save()
            return redirect('success')  
        else:
            print('Error:', product_form.errors)
    else:
        product_form = SupplierForms()

    return render(request, 'index.html', {'form': product_form})

def views_supplier(request:HttpRequest):
    view_supplier = Supplier.objects.all()
    return render(request , 'supplier/views_supplier.html',{'supplier':view_supplier})

def Update_Supplier(request: HttpRequest, supplier_id):
    supplier = Supplier.objects.get(pk=supplier_id)  
    if request.method == 'POST':
        supplier_form = SupplierForms(request.POST, request.FILES, instance=supplier)
        if supplier_form.is_valid():
            supplier_form.save()
            return redirect('Sipplier:Update_Supplier' , supplier_id )  
        else:
            print('Error:', supplier_form.errors)
    else:
        supplier_form = SupplierForms(instance=supplier) 

    return render(request, 'supplier/Update_Supplier.html',{'supplier':supplier})
def delet_supplier(request:HttpRequest , supplier_id):
    del_supplier = Supplier.objects.get(pk=supplier_id)
    if del_supplier.logo_Supplier:
        if os.path.isfile(del_supplier.logo_Supplier.path):
            os.remove()
    del_supplier.delete()
    return redirect('Supplier:views_supplier')
    