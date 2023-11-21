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


def edit_review(request, product_id, review_id):
    """Edit a review"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        review = Review.objects.filter(product=product).first()

        review_form = ReviewForm(request.POST, instance=review)

        if review_form.is_valid() and request.user == review.author:
                review = review_form.save()
                review.product = product
                review.save()
                reviews = Review.objects.filter(product=product)
                messages.success(request, "Your review has been successfully updated!")
                return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(request, "Your review has not been updated.")
    return redirect(reverse('product_detail', args=[product.id]))