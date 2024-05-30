from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'fullName', 'email', 'createdAt', 'phone', 'totalCost'
    list_display_links = 'fullName', 'email'
