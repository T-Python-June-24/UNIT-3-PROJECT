from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from Product.models import Product
from Supplier.models import Supplier
import plotly.express as px
def home_view(request: HttpRequest):
        return render(request, 'main/index.html')
def analytics_view(request: HttpRequest):


    ################# Stock chart######################

    product_queryset = Product.objects.all()
    names = [product.name for product in product_queryset]
    stocks = [product.stock for product in product_queryset]
    colors = [product.stock_status() for product in product_queryset]  # Get stock status for color coding
    product_ids = [product.id for product in product_queryset]

    color_map = {
        'In Stock': 'lightgreen',
        'Low Stock': 'red',
        'Out of Stock': 'grey'
    }
    bar_colors = [color_map[status] for status in colors]

    product_fig = px.bar(
        x=names,
        y=stocks,
        title="Current Stock Levels",
        labels={'x': "Product Name", 'y': "Stock Level"},
        color=bar_colors,
        color_discrete_map="identity",
        # hovertemplate='<a href="/detail/{product_ids}/"></a>',
    )
     
    product_fig.update_layout(
        title={
            'text': "Current Stock Levels",
            'font_size': 22,
            'xanchor': 'center',
            'x': 0.5
        }
    )

    low_stock_warning = "Attention: Some items are on Low Stock!" if 'Low Stock' in colors else ""
    product_chart = product_fig.to_html()

    ################# Suppliers chart######################
    
    supplier_queryset = Supplier.objects.all()
    supplier_names = [supplier.name for supplier in supplier_queryset]
    supplier_product_counts = [supplier.product_set.count() for supplier in supplier_queryset]

    supplier_fig = px.bar(
        x=supplier_names,
        y=supplier_product_counts,
        title="Number of Products per Supplier",
        labels={'x': "Supplier Name", 'y': "Number of Products"}
    )

    supplier_fig.update_layout(
        title={
            'text': "Number of Products per Supplier",
            'font_size': 22,
            'xanchor': 'center',
            'x': 0.5
        }
    )

    supplier_chart = supplier_fig.to_html()
   
 
    return render(request, 'main/analytics.html', {'product_chart': product_chart,'supplier_chart': supplier_chart,'low_stock_warning': low_stock_warning, })