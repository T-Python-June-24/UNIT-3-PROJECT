from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Category
from .forms import CategoryForm


# Create your views here.
def add_view(request: HttpRequest) -> HttpResponse:
    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category:all_view')
    else:
        print("not valid form", category_form.errors)
    return render(request, 'category/add.html', {'category_form': category_form})


def edit_view(request: HttpRequest, category_id: int) -> HttpResponse:
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
        else:
            print("not valid form", category_form.errors)
        return redirect('category:all_view')
    return render(request, 'category/edit.html', {"category": category})


def all_view(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, 'category/all.html', {"categories": categories})


def detail_view(request: HttpRequest, category_id: int) -> HttpResponse:
    category = Category.objects.get(id=category_id)
    return render(request, 'category/detail.html', {'category': category})


def delete_view(request: HttpRequest, category_id: int) -> HttpResponse:
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('category:all_view')
