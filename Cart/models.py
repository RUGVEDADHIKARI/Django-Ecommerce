from django.db import models
from base.models import BaseModel
from Products.models import *
from django.contrib.auth.models import User
from Cart.models import Coupon
# Create your models here.
class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    is_paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    def get_cart_total(self):
        cart_items=Cart_items.objects.all()
        price=[]
        for cart_item in cart_items:
            price.append(cart_item.price)
            if self.color_variant:
                color_variant_price=self.color_variant.color_price
                price.append(color_variant_price)
            if self.size_variant:
                size_variant_price=self.size_variant.size_price
                price.append(size_variant_price)
        return sum(price)
    def get_cart_total_price_after_coupon(self):
        total = self.get_cart_total()

        if total < self.coupon.minimum_amount:
            return total
        return total - self.coupon.discount_amount
class Cart_items(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='Cart_items')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    color_variant=models.ForeignKey(color_variant,on_delete=models.SET_NULL,blank=True,null=True)
    size_variant=models.ForeignKey(size_variant,on_delete=models.SET_NULL,blank=True,null=True)

    def get_product_price(self):
        price=[]
        if self.color_variant:
            color_variant_price=self.color_variant.color_price
            price.append(color_variant_price)
        if self.size_variant:
            size_variant_price=self.size_variant.size_price
            price.append(size_variant_price)
        return sum(price)