from django.contrib import admin
from django.forms.models import ModelChoiceField

from ingener1.models import NalichiTehniki


class NalichiTehnikiAdmin(admin.ModelAdmin):
    list_display = ['Campus', 'kabinet', 'category', 'Edizm', 'kodTMU', 'Naimenovanie', 'count', 'sostoyanie']
    list_filter = ['kabinet', 'sostoyanie', 'category']
    search_fields = ('kabinet',)
    list_per_page = 20
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        if request.user.role.title != 'admin' or (obj.id is not None and obj.user is None):
            obj.user = request.user
            obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.role.title != 'admin':
            queryset = queryset.filter(user=request.user)
        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field.name)
        if db_field.name == "Campus":
            queryset = request.user.role.campus.all()
            return ModelChoiceField(queryset, initial=request.user)
        return super(NalichiTehnikiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(NalichiTehniki, NalichiTehnikiAdmin)
