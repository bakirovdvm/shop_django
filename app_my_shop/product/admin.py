from django.contrib import admin
from .models import Product, ProductImage, ProductReview, ProductSpecifications, Tag


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductReviewInline(admin.StackedInline):
    model = ProductReview


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductReviewInline]

    list_display = [
        'pk',
        'title',
        'price',
        'date',
        'count',
        'freeDelivery',
    ]

    list_display_links = ['pk', 'title', 'price']
    search_fields = 'title', 'description', 'price'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(ProductImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'src', 'alt']
    list_display_list = ['pk', 'src', 'alt']


@admin.register(ProductReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'email', 'date']
    list_display_links = ['pk', 'author', 'email', 'date']


@admin.register(ProductSpecifications)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'value']
    list_display_links = ['pk', 'name', 'value']
