from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from Product.models import Product
import plotly.express as px

# Create your views here.

def home_view(request:HttpRequest):
    queryset=Product.objects.all()
    fig=px.bar(
        x=[q.name for q in queryset],
        y=[q.stock for q in queryset],
        title="Current Stock Levels",

        labels={'x':"Product Name","y":"Stock Level"}
    )
    fig.update_layout(title={
        'font_size':22,
        'xanchor':'center',
        'x':0.5
    })
    chart=fig.to_html()
    return render(request, 'main/index.html',{'chart':chart})

