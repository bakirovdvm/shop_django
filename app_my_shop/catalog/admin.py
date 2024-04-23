from django.contrib import admin
from .models import Category, Subcategory, CategoryImage, SubCategoryImage


class SubCategoryInline(admin.StackedInline):
    model = Subcategory


class CategoryImagesInline(admin.StackedInline):
    model = CategoryImage


class SubCategoryImagesInline(admin.StackedInline):
    model = SubCategoryImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline, CategoryImagesInline]
    list_display = 'id', 'title'
    list_display_links = 'id', 'title'
    search_fields = 'title', 'subcategory'


@admin.register(Subcategory)
class SubCategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryImagesInline]
    list_display = 'id', 'title'
    list_display_links = 'id', 'title'
    search_fields = 'id', 'title'


@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = "pk", "src", "alt", "category"
    list_display_links = "pk", "src"
    search_fields = "pk", "alt"


@admin.register(SubCategoryImage)
class SubCategoryImageAdmin(admin.ModelAdmin):
    list_display = "pk", "src", "alt", "subcategory"
    list_display_links = "pk", "src"
    search_fields = "pk", "alt"






