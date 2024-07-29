from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
import csv
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Category
from .forms import CategoryForm
from django.db.models import Count, Q, Sum

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10  # Number of categories per page

# this function is used to get the product count, and total quantity related to the category
    def get_queryset(self):
        queryset = Category.objects.annotate(
            product_count=Count('product'),
            total_quantity=Sum('product__quantity')
        )
        
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



# CRUD FUNCTIONS

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully.')
        else:
            messages.error(request, 'Category creation failed, check the fields correctly')
    return redirect('category_list')

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
        else:
            messages.error(request, 'Category update failed, check the fields correctly')
    return redirect('category_list')

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully.')
    return redirect('category_list')



# CSV RELATED FUNCTIONS

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


def export_categories_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="categories_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Description'])

    categories = Category.objects.all()
    if categories.exists():
        for category in categories:
            writer.writerow([category.name, category.description])
        messages.success(request, 'Categories exported successfully.')
    else:
        messages.warning(request, 'No categories found to export.')

    return response