from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Coupon)

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price']
    inlines=[ProductImageAdmin]

@admin.register(color_variant)
class color_variant(admin.ModelAdmin):
    list_display=['color_name','color_price']
    model=color_variant
@admin.register(size_variant)
class Size(admin.ModelAdmin):
    list_display=['size_name','size_price']
    model=size_variant

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
# Register your models here.
