from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from src.base.services import get_path_upload_product_image, validate_size_image


class Category(models.Model):
    """ Модель категорий """

    title = models.CharField(db_index=True, max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("title", )
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    """ Модель подкатегорий """
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="sub_category", verbose_name="Категория"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")

    def __str__(self):
        return f"{self.category} ({self.title})"

    class Meta:
        ordering = ("title", )
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    """ Модель товара """

    owner = models.ForeignKey(
        User, related_name="product_owner",
        on_delete=models.CASCADE, verbose_name="Владелец"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='product_category', verbose_name="Категория товара"
    )
    title = models.CharField(db_index=True, max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")
    picture = models.ImageField(
        upload_to=get_path_upload_product_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']),
            validate_size_image],
    )
    description = models.TextField(max_length=8000, verbose_name="Описание товара")
    available = models.BooleanField(default=True, verbose_name="Наличие на складе")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена товара")

    tags = TaggableManager(verbose_name="Тэги к товару")

    def __str__(self):
        return f"{self.owner} - {self.title}"

    class Meta:
        ordering = ("title", )
        index_together = (("id", "slug"), )
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductImage(models.Model):
    """ Модель для загрузки нескольких изображений для товара """

    picture = models.ImageField(
        upload_to=get_path_upload_product_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_size_image],
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_images", verbose_name="Изображения"
    )