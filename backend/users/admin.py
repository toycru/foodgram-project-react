from django.contrib.admin import ModelAdmin, register
# from django.contrib.auth.admin import ModelAdmin

from .models import GourmetUser


@register(GourmetUser)
class GourmetUserAdmin(ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email',
    )
    fields = (
        ('username', 'email', ),
        ('first_name', 'last_name', ),
    )

    search_fields = (
        'username', 'email',
    )
    list_filter = (
        'first_name', 'email',
    )
