import json

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Student, Tenant
from django.http import JsonResponse
from .models import Student
from django.shortcuts import get_object_or_404

def student_list(request, tenant_slug):
    tenant = get_object_or_404(Tenant, domain=tenant_slug)
    students = Student.objects.filter(tenant=tenant).values()
    return JsonResponse(list(students), safe=False)


class AddStudentView(View):
    @csrf_exempt
    def post(self, request, tenant_slug, *args, **kwargs):
        tenant = get_object_or_404(Tenant, domain=tenant_slug)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        date_of_birth = data.get('date_of_birth')

        if not all([first_name, last_name, email, date_of_birth]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        student = Student.objects.create(
            tenant=tenant,
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth
        )

        return JsonResponse({'message': 'Student created successfully', 'student_id': student.id}, status=201)

class AddTenantView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        # Extract tenant data from the request payload
        name = data.get('name')
        domain = data.get('domain')

        # Validate required fields
        if not name or not domain:
            return JsonResponse({'error': 'Missing required fields: name, domain'}, status=400)

        # Check if a tenant with the same domain already exists
        if Tenant.objects.filter(domain=domain).exists():
            return JsonResponse({'error': 'Tenant with this domain already exists'}, status=400)

        # Create a new tenant
        tenant = Tenant.objects.create(
            name=name,
            domain=domain
        )

        return JsonResponse({'message': 'Tenant created successfully', 'tenant_id': tenant.id}, status=201)