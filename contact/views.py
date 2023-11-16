from django.shortcuts import render


def contact(request):
    """View to show the contact us page"""
    return render(request, 'contact/contact.html')