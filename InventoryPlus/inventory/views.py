from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from products.models import Product
from products.models import Supplier
from products.forms import ProductStockForm
from categories.models import Category
from django.db.models import Q, F, Count, Avg, Sum, Max, Min
import plotly.express as px


def plotly_view(request):
    products = Product.objects.all()
    low_stock_list = []
    low_stock_products = []
    for product in products:
        if product.productStock < 200:

            low_stock_list.append(product.id)
       
    for product_id in low_stock_list:

        low_stock_products.append(products.filter(pk=product_id))

    print(low_stock_products)
    product_data = {
        'Product Name': [product.productName for product in products],
        'Stock': [product.productStock for product in products],
        'Price': [product.productPrice for product in products]
    }

    product_fig = px.bar(product_data, x='Product Name', y='Stock', title='Product Stock')
    product_graph_div = product_fig.to_html(full_html=False)

    suppliers = Supplier.objects.all()
    supplier_data = {
        'Supplier Name': [supplier.supplierName for supplier in suppliers],
        'Number of Products': [supplier.product_set.count() for supplier in suppliers]
    }

    supplier_fig = px.bar(supplier_data, x='Supplier Name', y='Number of Products', title='Products per Supplier')
    supplier_graph_div = supplier_fig.to_html(full_html=False)

    return render(request, 'inventory/home.html', {
        'product_graph_div': product_graph_div,
        'supplier_graph_div': supplier_graph_div,
        'low_stock_products':low_stock_products,

    })

def inventory(request:HttpRequest):

    products = Product.objects.all()
    opreations = products.aggregate(Sum("unitPrice"),Count("productStock"),Avg("productPrice"),Count("productName")) # total costs of products and avrage of prices
    total_cost = opreations["unitPrice__sum"] * opreations["productStock__count"]
    productSupplier = Supplier.objects.all()
    productCategory = Category.objects.all()

    return render(request, "inventory/inventory.html", {
        'products': products,
        'productSupplier': productSupplier,
        'productCategory':productCategory,
        'total_cost':total_cost,
        'avrage_prices':round(opreations["productPrice__avg"]),
        'numbers_of_products':opreations["productName__count"],
    })

def stock_update(request:HttpRequest, product_id):

    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':

        form = ProductStockForm(request.POST,instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "updated product stock successfully", "success")
        else:
            print(form.errors.as_text)
            messages.error(request, "Unable to update product stock. Please enter valid information", "danger")

    return redirect('inventory:inventory_view')
    

# def statistics(request:HttpRequest, product_id):

#     products = Product.objects.all()
#     print(products)

#     avg = reviews.aggregate(Avg("rating"))
#     print(avg)

#     return render(request, "inventory/inventory.html", {
#         'products': products,

#     })