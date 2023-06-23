from django.contrib import admin
from network.models import Network, Transfernetwork, Report


class NetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'Edizm', 'count']
    list_filter = ['title']
    search_fields = ['title__startswith']
    list_per_page = 10


admin.site.register(Network, NetworkAdmin)


class TransfernetworkTabularInline(admin.TabularInline):
    list_display = ['campus', 'network', 'faculty', 'kabinet', 'namKabinet', 'count', 'Report']
    model = Transfernetwork



# admin.site.register(Transfernetwork, TransfernetworkAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'reportitle', 'is_done', 'no_report']
    list_filter = ['id']
    list_per_page = 10
    # search_fields = ('reportitle', 'content')
    inlines = [TransfernetworkTabularInline]


admin.site.register(Report, ReportAdmin)
