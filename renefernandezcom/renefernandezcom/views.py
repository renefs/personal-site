# -*- coding: utf-8 -*-
__author__ = 'rene'

from django.shortcuts import render

from django.utils.translation import ugettext as _

from django.core.mail import send_mail
from renefernandezcom.forms import ContactForm

def home(request):
    form = contact(request)

    return render(request, 'home.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                '[Página personal] Formulario de contacto',
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['hola@renefernandez.com'],
            )

            new_form = ContactForm()
            new_form.success = _('El mensaje ha sido enviado correctamente. ¡Gracias!')

            return new_form
    else:
        form = ContactForm()
    return form