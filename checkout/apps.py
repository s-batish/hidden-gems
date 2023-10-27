from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Updates order totals automatically by calling update_total method
        every time a line item is saved or deleted
        """
        import checkout.signals
