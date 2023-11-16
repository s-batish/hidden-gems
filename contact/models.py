from django.db import models


class Contact(models.Model):
    """Model to generate the Contact Us form"""
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=1000, null=False, blank=False)
    date_sent = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_sent']

    def __str__(self):
        return f"Email by {self.name}: {self.date_sent}"
