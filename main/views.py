from django.shortcuts import render
from .models import MainBlock

def index(request):
    context = {
        'mainBlock': MainBlock.objects.first()
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')