from django.shortcuts import render
from .models import Service
# Create your views here.

def serviceList(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', { 'services': services})