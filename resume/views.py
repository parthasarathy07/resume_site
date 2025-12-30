from django.shortcuts import render
from .models import Resume

def dashboard(request):
    resume = Resume.objects.first()
    return render(request, 'resume/dashboard.html', {'resume': resume})
