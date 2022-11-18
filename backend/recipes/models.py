from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE

User = get_user_model()

class Recipe(models.Model):
    """Модель для рецептов."""
    title = models.CharField(
        'Название блюда',
        help_text='Введите название блюда',
        max_length=200
    )
    text = models.TextField(
        'Текст рецепта',
        help_text='Введите текст рецепта'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    tag = models.ForeignKey(
        "Tag",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='recipes',
        verbose_name='Тэг',
        help_text='Выберите тэг'
    )
    # Поле для картинки (необязательное)
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/',
        blank=True
    )

    def __str__(self):
       return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

class Tag(models.Model):
    """Тэги для рецептов.
    Связано с моделью Recipe через М2М.
    Поля `name` и 'slug` - обязательны для заполнения."""
    name = models.CharField(
        verbose_name='Тэг',
        max_length=200,
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цветовой HEX-код',
        max_length=6,
        blank=True,
        null=True,
        default='FF',
    )
    slug = models.SlugField(
        verbose_name='Слаг тэга',
        unique=True,
        max_length=200
    )

class Ingredient(models.Model):
    """Ингридиенты для рецепта.
    Связано с моделью Recipe через М2М (AmountIngredient)."""
    name = models.CharField(
        verbose_name='Ингридиент',
        max_length=200,
        unique=True,
    )
    measure = models.CharField(
        verbose_name='Единицы измерения',
        max_length=200
    )

class ingredientQuantity(models.Model):
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
                1, 'Нужно хоть какое-то количество.'
            ),
            MaxValueValidator(
                10000, 'Слишком много!'
            ),
        ),
    )
    

"""
class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
"""

class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )
