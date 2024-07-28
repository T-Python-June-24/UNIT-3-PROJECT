from django.shortcuts import render

# Create your views here.

def inventory_report(request):
    # Generate your inventory report data here
    report_data = {}
    return render(request, 'reports/inventory_report.html', report_data)

def supplier_report(request):
    # Generate your supplier report data here
    report_data = {}
    return render(request, 'reports/supplier_report.html', report_data)
