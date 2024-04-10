from django.contrib import admin
from .models import Profile, Avatar


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'pk', 'fullName', 'email', 'phone', 'balance'
    list_display_links = 'fullName', 'email',

    ordering = (
        'fullName',
        'pk'
    )

    search_fields = (
        'fullName',
        'email',
        'phone'
    )

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):

    list_display = "pk", "src", "alt"
    list_display_links = "pk", "alt"


