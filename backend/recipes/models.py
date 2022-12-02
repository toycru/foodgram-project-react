from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CASCADE, UniqueConstraint

from users.models import GourmetUser


class Tag(models.Model):
    """Тэги для рецептов.
    Связано с моделью Recipe через М2М."""
    name = models.CharField(
        verbose_name='Тэг',
        max_length=200,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг тэга',
        unique=True,
        max_length=200
    )
    color = models.CharField(
        verbose_name='Цветовой HEX-код',
        max_length=6,
        blank=True,
        null=True,
        default='FF',
    )


class Meta:
    verbose_name = 'Тэг'
    verbose_name_plural = 'Тэги'
    ordering = ('name', )


def __str__(self) -> str:
    return f'{self.name} (цвет: {self.color})'


class Recipe(models.Model):
    """Модель для рецептов.
    Связана с пользователем-автором GourmetUser через O2М.
    Связана с количеством игридиентов IngredientQuantity через O2М.
    Связана с пользователем Tags через M2М.
    Связана с GourmetUser через M2М для добавления в избронное и покупки."""
    author = models.ForeignKey(
        GourmetUser,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    name = models.CharField(
        'Название блюда',
        help_text='Введите название блюда',
        max_length=200
    )
    text = models.TextField(
        'Текст рецепта',
        help_text='Введите текст рецепта'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления, мин.',
        default=0,
        validators=(
            MinValueValidator(
                1,
                'Слишком быстро, так не бывает!'
            ),
            MaxValueValidator(
                600,
                'Слишком долго.'
            ),
        ),
    )
    image = models.ImageField(
        'Изображение блюда',
        upload_to='recipe_pictures/',
        blank=True,
        null=True,
    )
    create_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тэг',
    )
    is_favorite = models.ManyToManyField(
        GourmetUser,
        verbose_name='Избранное',
        related_name='favorites'
    )
    is_in_shopping_list = models.ManyToManyField(
        GourmetUser,
        verbose_name='Список покупок',
        related_name='shopping_list'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Ingredient(models.Model):
    """Ингридиенты для рецепта.
    Связана с моделью IngredientQuantity через O2М."""
    name = models.CharField(
        verbose_name='Ингридиент',
        max_length=200,
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=200
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}.'


class IngredientQuantity(models.Model):
    """Количество ингредиента в конкретном рецепте.
    Связана с Recipe через O2M
    Связана с Ingredient через М2М."""
    recipe = models.ForeignKey(
        verbose_name='В каких рецептах',
        related_name='ingredient',
        to=Recipe,
        on_delete=CASCADE,
    )
    ingredients = models.ForeignKey(
        verbose_name='Связанные ингредиенты',
        related_name='recipe',
        to=Ingredient,
        on_delete=CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=0,
        validators=(
            MinValueValidator(
                1, 'Слишком мало.'
            ),
            MaxValueValidator(
                10000, 'Слишком много.'
            ),
        ),
    )

    class Meta:
        ordering = ('recipe', )
        constraints = (
            UniqueConstraint(
                fields=('recipe', 'ingredients', ),
                name='\n%(app_label)s_%(class)s ingredient alredy added\n',
            ),
        )
