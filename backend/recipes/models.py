# from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE
from users.models import GourmetUser

# User = get_user_model()


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


class Recipe(models.Model):
    """Модель для рецептов.
    Связана с пользователем-автором GourmetUser через O2М.
    Связана с количеством игридиентов IngredientQuantity через O2М.
    Связана с пользователем Tags через M2М.
    Связана с GourmetUser через M2М для добавления в избронное и список покупок."""
    author = models.ForeignKey(
        GourmetUser,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    title = models.CharField(
        'Название блюда',
        help_text='Введите название блюда',
        max_length=200
    )
    text = models.TextField(
        'Текст рецепта',
        help_text='Введите текст рецепта'
    )
    cook_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        default=0,
        validators=(
            MinValueValidator(
                1,
                'Блюдо уже готово!'
            ),
            MaxValueValidator(
                600,
                'Ждать долго.'
            ),
        ),
    )
    image = models.ImageField(
        'Изображение блюда',
        upload_to='recipes/',
        blank=True
    )
    create_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )  
    tag = models.ForeignKey(
        Tag,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='recipes',
        verbose_name='Тэг',
        help_text='Выберите тэг'
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
       return self.title

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
        # unique=True,
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
    quantity = models.PositiveSmallIntegerField(
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