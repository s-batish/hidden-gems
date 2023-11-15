from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from products.models import Product


@login_required
def view_wishlist(request):
    """View to display the user's wishlist"""
    wishlist = Wishlist.objects.filter(user=request.user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }
    return render(request, template, context)


@login_required
def add_wishlist(request, product_id):
    """View to add a product to the wishlist"""
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist(user=request.user, product=product)

    # Checks if the item is already in the user's wishlist
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).exists()

    if wishlist_item:
        messages.warning(request, f"{product.name} is already in your wishlist.")
    else:
        wishlist.save()
        messages.success(request, f"{product.name} has been successfully added to your wishlist.")

    return redirect('wishlist')

@login_required
def delete_wishlist(request, product_id):
    """View to delete a product from the wishlist"""
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.filter(user=request.user, product=product)
    wishlist.delete()
    messages.success(request, f"{product.name} has been removed from your wishlist.")
    return redirect('wishlist')