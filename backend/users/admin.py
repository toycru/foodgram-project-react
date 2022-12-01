from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import GourmetUser

@register(GourmetUser)
class GourmetUserAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'password',
    )
    fields = (
        ('username', 'email', ),
        ('first_name', 'last_name', ),
    )
    fieldsets = []

    search_fields = (
        'username', 'email',
    )
    list_filter = (
        'first_name', 'email',
    )
