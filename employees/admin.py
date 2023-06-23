from django.contrib import admin

from employees.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Full_name', 'birthdate']



admin.site.register(Employee, EmployeeAdmin)