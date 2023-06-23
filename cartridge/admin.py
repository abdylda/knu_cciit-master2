from django.contrib import admin

from cartridge.models import Cartridge, Model, TransferCartridge


class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['title', 'model', 'foruseonaprinter', 'count']
    list_filter = ['title', 'model__title']
    list_per_page = 10


admin.site.register(Cartridge, CartridgeAdmin)

class ModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10


admin.site.register(Model, ModelAdmin)

class TransferCartridgeAdmin(admin.ModelAdmin):
    list_display = ['cartridge', 'campus', 'faculty', 'count', 'kabinet', 'namKabinet']
    list_filter = ['cartridge']
    list_per_page = 10

admin.site.register(TransferCartridge, TransferCartridgeAdmin)