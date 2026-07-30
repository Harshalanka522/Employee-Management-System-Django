from django.contrib import admin
from .models import Employee,Department


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'name', 'department', 'email', 'phone', 'joining_date']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
