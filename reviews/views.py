from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.views import View
from .forms import ReviewForm
from .models import Review


# # def add_review(request):
# #     """Add a review for a product"""

# #     if request.method == 'POST':
# #         form = ReviewForm(request.POST)
# #         if form.is_valid():
# #             review = form.save()
# #             messages.success(request, 'Successfully added product!')
# #             return redirect(reverse('add_review', args=[product.id]))
# #         else:
# #             messages.error(request, 'Failed to add product. Please ensure the form is valid.')
# #     else:
# #         form = ReviewForm()
        
# #     template = 'reviews/reviews.html'
# #     context = {
# #         'form': form,
# #     }

# #     return render(request, template, context)


# # class PostDetail(View):
# #     def post(self, request, slug, *args, **kwargs):

# #         queryset = Review.objects.filter(status=1)
# #         post = get_object_or_404(queryset, slug=slug)
# #         reviews = post.reviews.order_by("-created_on")

# #         review_form = ReviewForm(data=request.POST)
# #         if review_form.is_valid():
# #             review_form.instance.email = request.user.email
# #             review_form.instance.name = request.user.username
# #             review = review_form.save(commit=False)
# #             review.post = post
# #             review.save()
# #         else:
# #             review_form = ReviewForm()

# #         return render(
# #             request,
# #             "add_review.html",
# #             {
# #                 "post": post,
# #                 "reviews": reviews,
# #                 "review_form": review_form,
# #             },
# #         )


# from django.shortcuts import (render, get_object_or_404,
#                               redirect, reverse, HttpResponseRedirect)
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.utils import timezone

# # Internal:
# from .models import Review
# from .forms import ReviewForm
# from products.models import Product
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# @login_required
# def create_review(request):
#     """
#     view responsible for creating a product review
#     """
#     if request.method == 'POST':
#         product_id = int(request.POST['product_id'])
#         product = Product.objects.get(id=product_id)
#         username = request.POST['user']
#         body = request.POST['body']
#         current_time = request.POST['current_time']
#         user = User.objects.get(username=username)

#         review = Review.objects.create(
#             author=user,
#             product=product,
#             body=body,
#             time_posted=current_time
#         )

#         my_message = f'Review succesfully added'
#         data = {'id': review.id, 'author': review.author.username,
#                 'product': review.product.name, 'body': review.body,
#                 'time_posted': review.time_posted,  'message': my_message,
#                 'status': 'created'}
#     else:
#         error = {
#             'message': 'An Error ocurred!!'
#         }
#         return JsonResponse(error)

#     return JsonResponse(data)


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review')
            return redirect(reverse('add_review'))
        else:
            messages.error(request, 'Failed')
    else:
        form = ReviewForm()
        
    template = 'products/products/product_detail.html'
    context = {
        form: 'form',
    }

    return render(request, template, context)