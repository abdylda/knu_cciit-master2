from django.contrib import admin
from application.models import Application, Tender


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'document', 'accepted_application', 'no_report']

admin.site.register(Application, ApplicationAdmin)


class TenderAdmin(admin.ModelAdmin):
    list_display = ['name','document', 'purchase_order_is_ready', 'in_stock']

admin.site.register(Tender, TenderAdmin)