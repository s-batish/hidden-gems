# from django.shortcuts import render, reverse, get_object_or_404
# from django.contrib import messages
# from django.views import View
# from .forms import ReviewForm
# from .models import Review


# # # def add_review(request):
# # #     """Add a review for a product"""

# # #     if request.method == 'POST':
# # #         form = ReviewForm(request.POST)
# # #         if form.is_valid():
# # #             review = form.save()
# # #             messages.success(request, 'Successfully added product!')
# # #             return redirect(reverse('add_review', args=[product.id]))
# # #         else:
# # #             messages.error(request, 'Failed to add product. Please ensure the form is valid.')
# # #     else:
# # #         form = ReviewForm()
        
# # #     template = 'reviews/reviews.html'
# # #     context = {
# # #         'form': form,
# # #     }

# # #     return render(request, template, context)


from django.shortcuts import reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from products.models import Product

def add_review(request, product_id):
    """Add a review for a product"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
                Review.objects.create(
                    product=product,
                    author=request.user,
                    body=request.POST["body"],
                )
                reviews = Review.objects.filter(product=product)
                messages.success(request, "Your review has been successfully added!")
                return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(request, "Your review has not been submitted.")
    return redirect(reverse('product_detail', args=[product.id]))


def delete_review(request, product_id, review_id):
    """Delete a review"""
    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product=product).first()

    # Allows the authors of the review of staff members to delete
    if request.user == review.author or request.user.is_staff:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Your review has been successfully deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect(reverse('product_detail', args=[product.id]))