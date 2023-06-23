from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.forms.models import ModelChoiceField

from main.models import Faculty, NamKabinet, Kabinet, Campus, Edizm, Category, UserRole, User


# Register your models here.


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['title']


class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'role']

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Faculty, FacultyAdmin)

admin.site.register(User, UserAdmin)


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(UserRole, UserRoleAdmin)


class NamKabinetAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie']


admin.site.register(NamKabinet, NamKabinetAdmin)


class KabinetAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie', 'NamKabinet']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print( db_field.name)
        if db_field.name == "campus":
            queryset = request.user.role.campus.all()
            return ModelChoiceField(queryset, initial=request.user)
        return super(KabinetAdmin, self).formfield_for_foreignkey(db_field,
                                                                       request, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.role.title != 'admin':
            campus_ids = request.user.role.campus.all().values_list('id', flat=True)
            queryset = queryset.filter(campus_id__in=campus_ids)
        return queryset

admin.site.register(Kabinet, KabinetAdmin)


class CampusAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie']


admin.site.register(Campus, CampusAdmin)


class EdizmAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie']


admin.site.register(Edizm, EdizmAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie']


admin.site.register(Category, CategoryAdmin)






admin.site.site_title = "Администратор сайт Абдулла"
admin.site.site_header = "Администратор сайт Абдулла"