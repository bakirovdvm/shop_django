from django.contrib import admin
from .models import Basket, BasktetItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'session_key', 'created_at'
    list_display_links = 'id', 'user', 'created_at'


@admin.register(BasktetItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'product', 'basket', 'quantity', 'created_at'
    list_display_links = 'id', 'product', 'basket'

