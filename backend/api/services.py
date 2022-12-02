"""Дополнительные функции.
"""
from string import hexdigits

from rest_framework.serializers import ValidationError

from recipes.models import IngredientQuantity


def is_hex_color(value):
    """Проверяет - может ли значение быть HEX-цветом."""
    if len(value) not in (3, 6):
        raise ValidationError(
            f'{value} не правильной длины ({len(value)}).'
        )
    if not set(value).issubset(hexdigits):
        raise ValidationError(
            f'{value} не шестнадцатиричное.'
        )


def enter_ingredient_quantity_in_recipe(recipe, ingredients):
    """Записывает вложенные в рецепт ингредиенты .
    Создаёт объект IngredientQuantity связывающий объекты Recipe и
    Ingredient с указанием количества(`amount`) конкретного ингридиента.
    """
    for ingredient in ingredients:
        IngredientQuantity.objects.get_or_create(
            recipe=recipe,
            ingredients=ingredient['ingredient'],
            amount=ingredient['amount']
        )


def check_value_validate(value, klass=None):
    """Проверяет корректность переданного значения.
    Если передан класс, проверяет существует ли объект с переданным obj_id.
    При нахождении объекта создаётся Queryset[],
    для дальнейшей работы возвращается первое (и единственное) значение.
    """
    if not str(value).isdecimal():
        raise ValidationError(
            f'{value} должно содержать цифру'
        )
    if klass:
        obj = klass.objects.filter(id=value)
        if not obj:
            raise ValidationError(
                f'{value} не существует'
            )
        return obj[0]
