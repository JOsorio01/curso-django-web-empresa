from django.shortcuts import render
from .models import Service

def services(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, "services/services.html", context)
