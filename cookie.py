from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def set_cookie(request):
    response = HttpResponse("Setting your cookie")
    response.set_cookie('sensitive_cookie', 'sensitive data')
    return response 