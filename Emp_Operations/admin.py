from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
 	list_display = ('f_name', 'l_name', 'salary')

admin.site.register(Employee, EmployeeAdmin)
