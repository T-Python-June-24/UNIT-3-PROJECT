from django.contrib import admin
from .models import Product ,Supplier,Category
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class RecordAdmin(ImportExportModelAdmin):
    list_display=['name','description','expiry_date','stock','image','minimum_stock']
    
# Register your models here.
admin.site.register(Product,RecordAdmin)
