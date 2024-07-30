from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import ProtectedError  

from .models import Category
from .forms import CategoryForm

from django.contrib import messages  # Import messages
from .admin import CategoryResources

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
    if 'export' in request.POST:
        dataset = CategoryResources().export(categories)
        response_data = dataset.csv
        content_type = 'text/csv'

        response = HttpResponse(response_data, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="categories.csv"'
        return response
    
    return render(request, "Category/categories.html", {"categories" : categories
    , "search_term": searched if 'searched' in request.GET else ""     })

def category_added_success(request):
    return render(request, "Category/category_added_success.html")

def category_detail(request,category_id:int):

    category = Category.objects.get(pk=category_id)
    products = category.product_set.all()
    return render(request, 'Category/category_detail.html', {"category" : category , "products":products})
def category_update(request, category_id: int):
    category = Category.objects.get(pk=category_id)
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST, request.FILES, instance=category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('Category:category_page')

    return render(request, 'Category/category_detail.html', {'categoryForm': categoryForm, 'category': category})

def delete_category(request: HttpRequest, category_id: int):
    try:
        category = Category.objects.get(pk=category_id)
        
        category.delete()
        messages.success(request, "Category deleted successfully.")
        
    except ProtectedError as e:
        # Handle the case where the category cannot be deleted if it has products (protected)
        messages.error(request, "This category cannot be deleted because it has products ")
        
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")

    return redirect('Category:category_page')
