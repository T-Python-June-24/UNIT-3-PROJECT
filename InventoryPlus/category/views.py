from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Category
from .forms import CategoryForm


# Create your views here.
def add_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'category/add.html')


def edit_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'category/edit.html')


def all_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'category/all.html')


def detail_view(request: HttpRequest, category_id: int) -> HttpResponse:
    category = Category.objects.get(id=category_id)
    return render(request, 'category/detail.html', {'category': category})


def delete_view(request: HttpRequest, category_id: int) -> HttpResponse:
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('main:index_view')
