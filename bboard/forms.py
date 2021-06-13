from django.forms import ModelForm, MultiWidget, TextInput, Select, MultiValueField, ChoiceField, CharField
from django.contrib.auth.forms import UserCreationForm  
from django import forms
from .models import Bb, CustomUser
from django.urls import reverse_lazy

class PhoneWidget(MultiWidget):
    def __init__(self, code_length=3, num_length=7, attrs=None):
        widgets = [TextInput(attrs={'size': code_length, 'maxlength': code_length}),
                   TextInput(attrs={'size': num_length, 'maxlength': num_length})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def format_output(self, rendered_widgets):
        return '+7' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        else:
            return ['', '']



class PhoneField(MultiValueField):
    def __init__(self, code_length, num_length, *args, **kwargs):
        list_fields = [CharField(),
                       CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return '+7' + ' (' + values[0] + ') - ' + values[1][:3] + ' - ' + values[1][3:5] + ' - ' + values[1][5:]

class BbForm(ModelForm):
    
    class Meta:
        model = Bb
        fields = ['title', 'content', 'price', 'rubric', 'image', 'author', 'place']
        widgets = {'author': forms.HiddenInput(), 'phone': forms.HiddenInput()}

    

class SignUpForm(UserCreationForm):
    username = forms.CharField(label = "Имя пользователя", widget = forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label = "Имя", widget = forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    last_name=forms.CharField(label = "Фамилия", widget = forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    email=forms.EmailField(help_text = "Введите существующий адрес", label = "E-mail", widget = forms.EmailInput(attrs={'class': 'form-control'}), max_length=64)
    # password=forms.CharField(label = "Пароль", widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = PhoneField(code_length=3, num_length=7, help_text = "В первое поле введите код города, во второе - сам номер", label = "Номер телефона  +7 ")

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')
    