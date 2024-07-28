from django.shortcuts import render, get_object_or_404
from .models import Stock

# Create your views here.

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stock/stock_list.html', {'stocks': stocks})

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'stock/stock_detail.html', {'stock': stock})
