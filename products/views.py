from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm

from reviews.forms import ReviewForm
from reviews.models import Review
from wishlist.models import Wishlist


def all_products(request):
    """View to show all the products, including sorting and searching"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Code from https://stackoverflow.com/questions/71248375/filter-in-the-template-if-the-product-is-in-wishlist-or-no-django-ecommerce-web
    if request.user.is_authenticated:
        user=request.user
        wishlist = Wishlist.objects.filter(user=user)
        wishedProductsList = []
        for i in wishlist:
            wishedProductsList.append(i.product)
        count = Wishlist.objects.filter(user=request.user).count()
    else:
        wishlist = {}
        wishedProductsList = {}

    if request.GET:
        # Sorts the order of the products
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Sorts products by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Provides search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'wishedProductsList': wishedProductsList
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """View to show the product details"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    form = ReviewForm()
    template = 'products/product_detail.html'

    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()
        context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        'wishlist': wishlist,
        }
        return render(request, template, context)

    else:
        context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        }
        return render(request, template, context)

@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
