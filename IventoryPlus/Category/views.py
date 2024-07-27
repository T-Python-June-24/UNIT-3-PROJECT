from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Category
from .forms import CategoryForm

from django.contrib import messages  # Import messages


def add_category(request):
    categories = Category.objects.all()
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST, request.FILES)
        if categoryForm.is_valid():
            categoryForm.save()
            messages.success(request, 'Category added successfully!')
            return redirect("Category:category_added_success")
        else:
            for field, errors in categoryForm.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return render(request, "Category/add_category.html",{"categories" : categories})


def category_page(request:HttpRequest):

    categories = Category.objects.all()
    if 'searched' in request.GET:
        searched=request.GET['searched']
        if searched:
            categories=categories.filter(name__icontains=searched)

    return render(request, "Category/categories.html", {"categories" : categories
    , "search_term": searched if 'searched' in request.GET else ""                                                    })

def category_added_success(request):
    return render(request, "Category/category_added_success.html")

def category_detail(request,category_id:int):

    category = Category.objects.get(pk=category_id)

    return render(request, 'Category/category_detail.html', {"category" : category})
def category_update(request, category_id: int):
    category = Category.objects.get(pk=category_id)
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST, request.FILES, instance=category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('Category:category_detail', category_id=category.id)

    return render(request, 'Category/category_detail.html', {'categoryForm': categoryForm, 'category': category})

def delete_category(request:HttpRequest,category_id:int):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('Category:category_page')
