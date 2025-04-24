from django.urls import path
from .views import AddStudentView, AddTenantView, student_list

urlpatterns = [
    path('<str:tenant_slug>/students/', student_list, name='student_list'),
    path('<str:tenant_slug>/students/add/', AddStudentView.as_view(), name='add_student'),
    path('tenants/add/', AddTenantView.as_view(), name='add_tenant'),
]
