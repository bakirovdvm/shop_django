from django.contrib import admin
from .models import Basket, BasktetItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = 'user', 'session_key', 'created_at'
    list_display_links = 'user', 'session_key', 'created_at'
