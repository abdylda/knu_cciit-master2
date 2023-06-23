from django.contrib import admin
from doc.models import Documentation

# Register your models here.
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ['name','document']




admin.site.register(Documentation, DocumentationAdmin)