from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """View to show the bag page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Adjust the quantity of an item in the bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, item_id):
    """Remove an item from the bag"""

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
