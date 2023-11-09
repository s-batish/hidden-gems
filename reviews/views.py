from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm
from django.contrib import messages


class AddReview(LoginRequiredMixin, CreateView):
    """
    View to add a review
    """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = 'product_detail'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, 'Your review has been saved!')
        return super(AddReview, self).form_valid(form)