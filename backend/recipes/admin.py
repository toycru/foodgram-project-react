from django.contrib import admin, ModelAdmin, register

from .models import AmountIngredient, Ingredient, Recipe, Tag

EMPTY_VALUE_DISPLAY = 'Значение не задано'

@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = (
        'title', 'measure',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'title',
    )

    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'title', 'author', 'get_image',
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

    # inlines = (IngredientInline,)
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.image.url} width="80" hieght="30"')

    # get_image.short_description = 'Изображение'


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        'name', 'color', 'slug',
    )
    search_fields = (
        'name', 'color'
    )

    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY
