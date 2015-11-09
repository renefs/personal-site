# -*- coding: utf-8 -*-
__author__ = 'rene'
from renefernandezcom.settings import DEFAULT_FROM_EMAIL
from django.shortcuts import render

from django.utils.translation import ugettext as _

from django.contrib import messages
from django.core.mail import EmailMessage
from renefernandezcom.forms import ContactForm


def home(request):
    form = contact(request)

    return render(request, 'home.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            html_content = '<p>Nombre: <strong>' + cd['name'] + '</strong><p><strong>Email del remitente:</strong></p><p>' + \
                           cd['email'] + '</p><p><strong>Cuerpo:</strong></p>' + cd['message'] + '</p>'

            msg = EmailMessage('[Página personal] Formulario de contacto', html_content, DEFAULT_FROM_EMAIL,[DEFAULT_FROM_EMAIL])
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            new_form = ContactForm()
            messages.add_message(request, messages.SUCCESS,  _(u'El mensaje ha sido enviado correctamente. ¡Gracias!'))

            return new_form
    else:
        form = ContactForm()
    return form


def curriculum(request):

    return render(request, 'curriculum.html')