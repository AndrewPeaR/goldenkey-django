from django.shortcuts import render

from .forms import UserForm, ReviewForm, checkCaptcha
from .models import MainBlock, WelcomeBlock, Advantages, Performance, PerformanceItems, Memo, FAQ, News, Reviews, DocumentsPage, Filials, FilialsNews, FilialsTeam


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
        'filials': Filials.objects.all(),
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
    context = {
        'docsBlocks': DocumentsPage.objects.all()
    }
    return render(request, 'main/aboutFull.html', context)

def goldenkey(request):
    context = {
        'docsBlocks': DocumentsPage.objects.filter(page=DocumentsPage.Pages.GOLDENKEY)
    }
    return render(request, 'main/about.html', context)

def bashaeva(request):
    context = {
        'docsBlocks': DocumentsPage.objects.filter(page=DocumentsPage.Pages.BASHAEVA)
    }
    return render(request, 'main/about.html', context)

def filial(request, filial_slug):
    filialId = Filials.objects.filter(slug=filial_slug)[0].id
    context = {
        'filial': Filials.objects.filter(slug=filial_slug)[0],
        'filial_news': FilialsNews.objects.filter(filials_id=filialId)
    }
    return render(request, 'main/filial.html', context)