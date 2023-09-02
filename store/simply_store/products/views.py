from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, render

from products.models import Basket, Product, ProductCategory


User = get_user_model()


def index(request):
    context = {'is_promotion': True}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(
        category_id=category_id) if category_id else Product.objects.all()
    per_page = 6
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'categories': ProductCategory.objects.all(),
        'products': products_paginator}
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])