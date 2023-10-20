from django.shortcuts import render


def view_bag(request):
    """View to show the bag pag"""
    return render(request, 'bag/bag.html')
