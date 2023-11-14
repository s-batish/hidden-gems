from django.shortcuts import render, reverse
from .models import Wishlist
from products.models import Product

def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)


# def add_wishlist(request, product_id):
#     """View to add a product to the wishlist"""
#     product = get_object_or_404(Product, pk=product_id)
#     wishlist = get_object_or_404(Wishlist, user=request.user.id)
    
#     if wishlist.product.filter(id=request.user.id).exists():
#         wishlist.product.remove(request.user)
#     else:
#         wishlist.product.add(request.user)
#     return redirect(reverse('product_detail', args=[product.id]))

#     # if product in wishlist.products.all():
#     #     messages.info(request, f"{product.title} is already on your Wishlist!")
#     # else:
#     #     wishlist.products.add(product)
#     #     messages.info(request, f"{product.title} has been added to your Wishlist!")