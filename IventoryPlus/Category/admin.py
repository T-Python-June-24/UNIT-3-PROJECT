from django.contrib import admin
from .models import Category
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class CategoryResources(resources.ModelResource):
    class Meta:
        model=Category
        fields =('name','info')
class RecordAdmin(ImportExportModelAdmin):
    resource_class =CategoryResources
    list_display=['name','info']

admin.site.register(Category,RecordAdmin)