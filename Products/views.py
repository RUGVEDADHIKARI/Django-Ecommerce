from django.shortcuts import render
from Products.models import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def get_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    selected_size = request.GET.get("size")
    updated_price = None

    if selected_size:
        try:
            updated_price = product.get_product_price_by_size(selected_size)
        except size_variant.DoesNotExist:
            selected_size = None  # invalid size, reset

    context = {
        "product": product,
        "selected_size": selected_size,
        "updated_price": updated_price,
    }
    return render(request, "Products/Products.html", context)

