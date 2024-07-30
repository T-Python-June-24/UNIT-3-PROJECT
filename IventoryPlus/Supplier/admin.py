from django.contrib import admin
from .models import Supplier
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class RecordAdmin(ImportExportModelAdmin):
    list_display=['name','email','logo','phone_number','website','description']
admin.site.register(Supplier,RecordAdmin)