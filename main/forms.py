from django import forms

class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"questions__form-input", 'placeholder': 'Имя'}), label='')
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={"class":"questions__form-input", 'placeholder': '+7(___)___-__-__'}), label='')
    question = forms.CharField(widget=forms.Textarea(attrs={"class":"questions__form-input", 'placeholder': 'Вопрос'}), label='')