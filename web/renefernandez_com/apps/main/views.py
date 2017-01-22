import sys
from django.shortcuts import render, redirect

from renefernandez_com.apps.main.forms import ContactForm
from django.utils.translation import ugettext as _
from django.core.mail import EmailMessage
from django.contrib import messages
from renefernandez_com.settings import DEFAULT_FROM_EMAIL


def home(request):
    form = process_contact_form(request)

    return render(request, 'home.html', {'form': form})


def process_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("Form is valid")
            cd = form.cleaned_data

            html_content = '<p>Nombre: <strong>' + cd['name'] \
                           + '</strong><p><strong>Email del remitente:</strong></p><p>' + \
                           cd['email'] + '</p><p><strong>Cuerpo:</strong></p>' + cd['message'] + '</p>'

            msg = EmailMessage('[Página personal] Formulario de contacto', html_content, DEFAULT_FROM_EMAIL,
                               [DEFAULT_FROM_EMAIL])
            msg.content_subtype = "html"  # Main content is now text/html
            if 'test' not in sys.argv:
                msg.send()

            new_form = ContactForm()
            messages.add_message(request, messages.SUCCESS, _(u'El mensaje ha sido enviado correctamente. ¡Gracias!'))

            return new_form
        else:
            print("Form is invalid")
    else:
        form = ContactForm()
    return form
