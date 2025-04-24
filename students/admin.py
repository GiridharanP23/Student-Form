from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Tenant

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'tenant']
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Student, StudentAdmin)
admin.site.register(Tenant)