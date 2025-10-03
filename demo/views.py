from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import platform
import sys

def home(request):
    """Home page view with system information"""
    context = {
        'title': 'Django Demo App',
        'current_time': timezone.now(),
        'python_version': sys.version,
        'platform': platform.platform(),
        'django_version': '4.2.24',
    }
    return render(request, 'demo/home.html', context)

def about(request):
    """About page view"""
    return render(request, 'demo/about.html', {
        'title': 'About - Django Demo App'
    })

def api_status(request):
    """Simple API endpoint for health check"""
    return HttpResponse("{'status': 'ok', 'message': 'Django Demo App is running!'}", content_type='application/json')
