from django.contrib import admin
from .models import Category
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class RecordAdmin(ImportExportModelAdmin):
    list_display=['name','info']

admin.site.register(Category,RecordAdmin)