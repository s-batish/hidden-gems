from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model to add reviews on products
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)
    body = models.TextField(max_length=500, null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Review by {self.author}: {self.body}"
