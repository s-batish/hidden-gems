from .models import Wishlist


def wishlist_contents(request):
    """Context to show total number of items in wishlist"""
    context = {}
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
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
