# from django.shortcuts import render, get_object_or_404
# from django.views import View
# from .forms import ReviewForm
# from .models import Review


# def add_review(request):
#     """Add a review for a product"""

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save()
#             messages.success(request, 'Successfully added product!')
#             return redirect(reverse('add_review', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to add product. Please ensure the form is valid.')
#     else:
#         form = ReviewForm()
        
#     template = 'reviews/reviews.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)


# class PostDetail(View):
#     def post(self, request, slug, *args, **kwargs):

#         queryset = Review.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         reviews = post.reviews.order_by("-created_on")

#         review_form = ReviewForm(data=request.POST)
#         if review_form.is_valid():
#             review_form.instance.email = request.user.email
#             review_form.instance.name = request.user.username
#             review = review_form.save(commit=False)
#             review.post = post
#             review.save()
#         else:
#             review_form = ReviewForm()

#         return render(
#             request,
#             "add_review.html",
#             {
#                 "post": post,
#                 "reviews": reviews,
#                 "review_form": review_form,
#             },
#         )