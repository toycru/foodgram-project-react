from django.contrib.admin import ModelAdmin, TabularInline, register
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ingredient, Recipe, Tag, IngredientQuantity

EMPTY_VALUE_DISPLAY = 'Значение не задано'


class IngredientInline(TabularInline):
    model = IngredientQuantity
    extra = 2

@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'color', 'slug',
    )
    search_fields = (
        'name', 'color'
    )

    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY


@register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'measurement_unit',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )

    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY


@register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', # 'get_image',
    )
    fields = (
        ('title', 'cooking_time',),
        ('author', 'tags',),
        ('text',),
        ('image',),
    )
    raw_id_fields = ('author', )
    search_fields = (
        'title', 'author',
    )
    list_filter = (
        'title', 'author__username',
    )

    inlines = (IngredientInline,)
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" hieght="30"')

    # get_image.short_description = 'Изображение'



