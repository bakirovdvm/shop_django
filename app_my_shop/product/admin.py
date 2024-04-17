from django.contrib import admin
from .models import Product, ProductImage, ProductReview, ProductSpecifications, Tag


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'date',
        'count',
        'freeDelivery',
    ]

    list_display_links = ['title', 'price']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

