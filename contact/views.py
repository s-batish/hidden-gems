from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """View to show the contact us page and to create the functionality to send emails"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent.')
            return render(request, 'home/index.html')

    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)