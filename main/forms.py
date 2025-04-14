from dotenv import load_dotenv
load_dotenv()

from django import forms
from .models import Questions, Reviews, BookSend, ExcursionFilial

import os
import sys
import json
import requests

class BookForm(forms.Form, forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"sendbook__input", 'placeholder': 'Имя'}), label='', required=True)
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={"class":"sendbook__input", 'placeholder': '+7(___)___-__-__'}), label='', required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"sendbook__input", 'placeholder': 'Email'}), label='', required=True)
    policy = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"sendbook__checkbox", 'id': 'sendbook__input-policy'}), label='', required=True)

    class Meta:
        model = BookSend
        fields = ('name', 'phoneNumber', 'email', 'policy')

class ExcursionFilialForm(forms.Form, forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"filial__input", 'placeholder': 'Имя'}), label='', required=True)
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={"class":"filial__input", 'placeholder': '+7(___)___-__-__'}), label='', required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"filial__input", 'placeholder': 'Email'}), label='', required=True)
    policy = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"filial__checkbox", 'id': 'filial__input-policy'}), label='', required=True)

    class Meta:
        model = ExcursionFilial
        fields = ('name', 'phoneNumber', 'email', 'policy')

class UserForm(forms.Form, forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"questions__form-input", 'placeholder': 'Имя'}), label='')
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={"class":"questions__form-input", 'placeholder': '+7(___)___-__-__'}), label='')
    question = forms.CharField(widget=forms.Textarea(attrs={"class":"questions__form-input", 'placeholder': 'Вопрос'}), label='')

    class Meta:
        model = Questions
        fields = ('name', 'phoneNumber', 'question')

class ReviewForm(forms.Form, forms.ModelForm):
    name = forms.CharField()
    parent = forms.CharField()
    childAge = forms.CharField()
    review = forms.CharField()
    file = forms.FileField()
    class Meta:
        model = Reviews
        fields = ('name', 'parent', 'childAge', 'review', 'file')

# Запрос на проверку введеной капчи
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def checkCaptcha(request, type):
    match type:
        case 'question':
            secret=os.getenv('SMARTCAPTCHA_SERVER_KEY')
        case 'sendBook':
            secret=os.getenv('KEY_HIDE')
        case 'excursionFilial':
            secret=os.getenv('FILIAL_FORM_KEY')
        # case 'excursionForm':
        #     secret=os.getenv('EXCURSION_FORM_KEY')
    
    resp = requests.post(
       "https://smartcaptcha.yandexcloud.net/validate",
       data={           
          "secret": secret,
          "token": request.POST.get("smart-token"),
          "ip": get_client_ip(request)
       },
       timeout=1
    )
    
    server_output = resp.content.decode()
    if resp.status_code != 200:
       print(f"Allow access due to an error: code={resp.status_code}; message={server_output}", file=sys.stderr)
       return True
    return json.loads(server_output)["status"] == "ok"

