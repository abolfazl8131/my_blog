from blogBI.models import IPAddress

class SaveIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        try:
            ip_addr = IPAddress.objects.get(ip_address = ip)
        except IPAddress.DoesNotExist:
            ip_addr = IPAddress(ip_address = ip)
            ip_addr.save()

        request.ip_address = ip_addr
        
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response