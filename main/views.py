from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.core import serializers

import json
from .forms import UserForm, ReviewForm, checkCaptcha, BookForm, ExcursionFilialForm
from .models import MainBlock, WelcomeBlock, Advantages, Performance, PerformanceItems, Memo, FAQ, News, Reviews, DocumentsPage, Filials, FilialsNews, FilialsTeam, EmailSettings


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if checkCaptcha(request, 'question'):
                question = form.save(commit=False)
                question.save()
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
        'reviewForm': ReviewForm(),
        'sendBookForm': BookForm(),
    }
    return render(request, 'main/index.html', context)

def sendBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            if checkCaptcha(request, 'sendBook'):
                bookSend = form.save(commit=False)
                bookSend.save()
                email_settings = EmailSettings.objects.first()
                mail = EmailMessage(email_settings.theme, email_settings.body, 'noreply@goldenkey86.ru', to=[bookSend.email])
                mail.attach_file(email_settings.pdf.path)
                mail.send()
            else:
                print("Robot")
        else:
            print('Form invalid')
    return redirect('/')

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
    if request.method == 'POST':
        form = ExcursionFilialForm(request.POST)
        if form.is_valid():
            if checkCaptcha(request, 'excursionFilial'):
                excursionFilial = form.save(commit=False)
                excursionFilial.filial = Filials.objects.filter(slug=filial_slug)[0]
                excursionFilial.save()
            else:
                print("Robot")
        else:
            print('Form invalid')
    
    filialId = Filials.objects.filter(slug=filial_slug)[0].id
    context = {
        'filial': Filials.objects.filter(slug=filial_slug)[0],
        'filial_news': FilialsNews.objects.filter(filials_id=filialId),
        'filial_team': FilialsTeam.objects.filter(filials_id=filialId),
        'filial_form': ExcursionFilialForm(),
    }
    return render(request, 'main/filial.html', context)

def teamFilial(request):
    # print( json.loads(request.body)['teamId'])
    teamId = json.loads(request.body)['teamId']
    teamFilial = FilialsTeam.objects.filter(pk=teamId)
    # context = json.dumps(list(teamFilial), cls=DjangoJSONEncoder)
    context = serializers.serialize('json', teamFilial)
    # context = {
    #     'teamFilial': FilialsTeam.objects.get(pk=teamId),
    # }
    return JsonResponse(context, safe=False)