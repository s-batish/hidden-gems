from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


def contact(request):
    """
    View to show the contact us page and to create the functionality to send
    emails
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email_subject = form.cleaned_data['subject']
            user_message = form.cleaned_data['message']
            success_message = render_to_string(
                'contact/confirmation_email/confirmation_email.txt',
                {'name': name, 'user_message': user_message})
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]
            send_mail(
                email_subject,
                success_message,
                email_from,
                email_to
            )
            messages.success(request, 'Your message has been sent.')
            return render(request, 'home/index.html')

    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
