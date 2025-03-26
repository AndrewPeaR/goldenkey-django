from django.shortcuts import render
from .models import MainBlock, WelcomeBlock, Advantages

def index(request):
    context = {
        'mainBlock': MainBlock.objects.first(),
        'welcomeBlock': WelcomeBlock.objects.first(),
        'advantages': Advantages.objects.all()[:3]
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')