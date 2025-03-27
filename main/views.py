from django.shortcuts import render

from .forms import UserForm, ReviewForm, checkCaptcha
from .models import MainBlock, WelcomeBlock, Advantages, Performance, PerformanceItems, Memo, FAQ, News, Reviews


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if checkCaptcha(request):
                question = form.save(commit=False)
                question.save()
                # print("Passed and save form")
            else:
                print("Robot")
        else:
            print('Form invalid')
            
    
    context = {
        'mainBlock': MainBlock.objects.first(),
        'welcomeBlock': WelcomeBlock.objects.first(),
        'advantages': Advantages.objects.all()[:3],
        'performance': Performance.objects.first(),
        'performanceItems': PerformanceItems.objects.all(),
        'memo': Memo.objects.all(),
        'faq': FAQ.objects.all(),
        'news': News.objects.all(),
        'reviews': Reviews.objects.filter(published = True),
        'form': UserForm(),
        'reviewForm': ReviewForm()
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')