from django.shortcuts import render
from .models import Cart, Cart_items
from Products.models import Product, size_variant, Coupon
from django.http import HttpResponseRedirect
from django.contrib import messages


def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    user = request.user
    product = Product.objects.get(uid=uid)

    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_item = Cart_items.objects.create(cart=cart, product=product)

    if variant:
        variant = request.GET.get('variant')
        size_variant = size_variant.objects.get(size_name=variant)
        cart_item.size_variant = size_variant
        cart_item.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_page(request):
    cart_obj = Cart.objects.get(is_paid=False, user=request.user)

    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        coupon_obj = Coupon.objects.filter(coupon_code__exact=coupon)

        if not coupon_obj.exists():
            messages.warning(request, 'Invalid coupon code.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        if cart_obj.coupon:
            messages.warning(request, 'Coupon already exists.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        if coupon_obj[0].is_expired:
            messages.warning(request, 'Coupon code expired.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        if cart_obj.get_cart_total() < coupon_obj[0].minimum_amount:
            messages.warning(
                request, f'Amount should be greater than {coupon_obj.minimum_amount}')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        cart_obj.coupon = coupon_obj[0]
        cart_obj.save()

        messages.success(request, f'Coupon applied.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {'cart': cart_obj}
    return render(request, 'carts/cart.html', context)


def remove_cart_item(request, uid):
    try:
        cart_item = Cart_items.objects.get(uid=uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_coupon(request, cart_id):
    cart = Cart.objects.get(uid=cart_id)
    cart.coupon = None
    cart.save()

    messages.success(request, f'Coupon applied.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])