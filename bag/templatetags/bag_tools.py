from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculates the subtotal for each item"""
    return price * quantity
