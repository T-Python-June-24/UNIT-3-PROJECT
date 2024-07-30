from django.contrib import admin
from .models import Product ,Supplier,Category
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources,widgets
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import DateWidget

# Register your models here.

class ProductResource(resources.ModelResource):
    category=fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name')
    )
    #avoid raising an error when date is import from csv 
    expiry_date = fields.Field(
        column_name='expiry_date',
        attribute='expiry_date',
        widget=DateWidget(format='%d/%m/%Y')  
    )

    class Meta:
        model=Product
        fields = ('id', 'name', 'description', 'category', 'expiry_date', 'stock', 'image', 'minimum_stock')  

class RecordAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display=['name','description',"category",'expiry_date','stock','image','minimum_stock']
    
# Register your models here.
admin.site.register(Product,RecordAdmin)



