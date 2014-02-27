__author__ = 'rene'

from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': 'form-control'}))