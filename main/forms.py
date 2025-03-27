from dotenv import load_dotenv
load_dotenv()

from django import forms
from .models import Questions, Reviews

import os
import sys
import json
import requests

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

def checkCaptcha(request):
    resp = requests.post(
       "https://smartcaptcha.yandexcloud.net/validate",
       data={
          "secret": os.getenv('SMARTCAPTCHA_SERVER_KEY'),
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

