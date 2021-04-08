from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django import forms
from .models import Bb, CustomUser
from django.urls import reverse_lazy

class BbForm(ModelForm):
    
    class Meta:
        model = Bb
        fields = ['title', 'content', 'price', 'rubric', 'image', 'phone', 'author', 'place']
        widgets = {'author': forms.HiddenInput()}

class SignUpForm(UserCreationForm):
    username = forms.CharField(label = "Имя пользователя", widget = forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label = "Имя", widget = forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    last_name=forms.CharField(label = "Фамилия", widget = forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    email=forms.EmailField(help_text = "Введите существующий адрес", label = "E-mail", widget = forms.EmailInput(attrs={'class': 'form-control'}), max_length=64)
    password1=forms.CharField(label = "Пароль", widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(help_text = "Пароли должны совпадать", label = "Повторите пароль", widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
    