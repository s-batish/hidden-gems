from django.shortcuts import (render,
                              get_object_or_404, HttpResponseRedirect,
                              redirect, reverse)
from .models import Wishlist


def wishlist_contents(request):
    """Context to show totla number of items in wishlist"""
    wishlist = Wishlist.objects.filter(user=request.user)
    if request.user.is_authenticated:
        wishlist_count = wishlist.count()
        context = {
            'wishlist_count': wishlist_count,
        }
    else:
        wishlist_count = 0
        context = {
            'wishlist_count': wishlist_count,
        }
    return context