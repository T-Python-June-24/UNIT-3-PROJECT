from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from products.models import Product,Supplier,Category
from datetime import datetime,timedelta
from django.template.loader import render_to_string
from weasyprint import HTML



def home_view(request:HttpRequest):

    products = Product.objects.all().order_by("product_name")
    suppliers = Supplier.objects.all().order_by("supplier_name")
    categories = Category.objects.all().order_by("name")

    # Calculate the date 10 days from today
    ten_days_from_today = datetime.now().date()+ timedelta(days=10)
    # Filter products with expiry_date less than or equal to 10 days from today
    ex_products = Product.objects.filter(expiry_date__lte=ten_days_from_today).order_by('product_name')

    low_level_products = Product.objects.filter(stock_level__lte=10).order_by("product_name")

    return render(request, 'main/index.html', {"products" : products,"suppliers": suppliers, 'categories': categories, 'ex_products':ex_products, 'low_level_products':low_level_products})


def suppliers_report_view(request:HttpRequest):
    # Query the suppliers
    suppliers = Supplier.objects.all().order_by('supplier_name')
    # Get the current date
    current_date = datetime.now().strftime('%B %d, %Y')  # Format as needed
    
    # Render the template to a string
    html_string = render_to_string('main/suppliers_report.html', {'suppliers': suppliers,'current_date':current_date})
    
    # Generate the PDF
    pdf_file = HTML(string=html_string, base_url="/").write_pdf()
    
    # Create an HTTP response with the PDF file
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="suppliers_report.pdf"'
    
    return response


def contact_view(request:HttpRequest):

    return render(request, 'main/contact.html' )



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response
