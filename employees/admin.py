from django.contrib import admin

from .models import Department, Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'department', 'position', 'salary')
    list_filter = ('department__name',)
    search_fields = ('first_name', 'last_name', 'surname', 'position')


admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)
