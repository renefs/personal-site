from django import forms
from django.utils.translation import ugettext as _
from captcha.fields import ReCaptchaField

# from captcha.fields import CaptchaField, CaptchaTextInput


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': _('form_name_placeholder')}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control input-lg', 'type': 'email', 'placeholder': 'Email'}))
    captcha = ReCaptchaField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control input-lg', 'placeholder': _('form_message_placeholder')}))
