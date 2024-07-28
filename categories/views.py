from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import csv
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Category
from django import forms
import csv
from .forms import CategoryForm
from django.db.models import Count, Q

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10  # Number of categories per page

    def get_queryset(self):
        queryset = Category.objects.annotate(product_count=Count('product'))
        
        # Search functionality
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )
        
        # Sorting
        sort = self.request.GET.get('sort', 'name')
        if sort == 'name':
            queryset = queryset.order_by('name')
        elif sort == '-name':
            queryset = queryset.order_by('-name')
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        context['search_query'] = self.request.GET.get('search', '')
        context['current_sort'] = self.request.GET.get('sort', 'name')
        return context

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Category created successfully.')
            except forms.ValidationError as e:
                messages.error(request, str(e))
                return render(request, 'categories/category_list.html', {'form': form})
    else:
        form = CategoryForm()
    return redirect('category_list')

def export_categories_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="categories_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Description'])

    categories = Category.objects.all()
    for category in categories:
        writer.writerow([category.name, category.description])

    return response

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Category updated successfully.')
            except forms.ValidationError as e:
                messages.error(request, str(e))
                return render(request, 'categories/category_form.html', {'form': form})
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('category_list')

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
    return redirect('category_list')

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
    return redirect('category_list')
def import_categories_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.lower().endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
            return redirect('category_list')

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        required_columns = {'name', 'description'}
        if not required_columns.issubset(map(str.lower, reader.fieldnames)):
            messages.error(request, 'CSV file must contain Name and Description columns matching the Category model.')
            return redirect('category_list')

        try:
            for row in reader:
                Category.objects.update_or_create(
                    name=row['name'],
                    defaults={'description': row['description']}
                )
        except Exception as e:
            messages.error(request, f'Error processing CSV file: {str(e)}')
            return redirect('category_list')

        messages.success(request, 'Categories imported successfully.')
    return redirect('category_list')