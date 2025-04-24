from django.urls import path
from .views import student_list, AddStudentView, AddTenantView

urlpatterns = [
    path('students/add/', AddStudentView.as_view(), name='add_student'),
    path('students/', student_list, name='student-list'),
    path('tenants/add/', AddTenantView.as_view(), name='add_tenant'),
]
