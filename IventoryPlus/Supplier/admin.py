from django.contrib import admin
from .models import Supplier
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.



class SupplierResource(resources.ModelResource):

    class Meta:
        model=Supplier
        fields = ('id', 'name', 'email', 'logo', 'phone_number', 'website', 'image', 'description')  

class RecordAdmin(ImportExportModelAdmin):
    resource_class = SupplierResource
    list_display=['name','email','logo','phone_number','website','description']
    
admin.site.register(Supplier,RecordAdmin)

