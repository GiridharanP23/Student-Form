from django.http import HttpResponseForbidden
from .models import Tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract the tenant domain from the query parameter
        tenant_domain = request.GET.get('tenant_domain')
        print(f"Tenant domain from query param: {tenant_domain}")

        if not tenant_domain:
            return HttpResponseForbidden("Tenant domain not provided.")

        try:
            tenant = Tenant.objects.get(domain=tenant_domain)
            request.tenant = tenant  # Attach tenant to request
        except Tenant.DoesNotExist:
            return HttpResponseForbidden("Tenant not found.")

        return self.get_response(request)
