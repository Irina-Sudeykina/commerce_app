from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", help_text="Введите название категории")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование продукта", help_text="Введите наименование продукта"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="catalog",
        verbose_name="Категория",
        help_text="Введите категорию продукта",
    )
    price = models.FloatField(verbose_name="Цена продукта", help_text="Введите цену продукта")
    created_at = models.DateField(
        blank=True, auto_now_add=True, verbose_name="Дата создания", help_text="Укажите дату создания"
    )
    updated_at = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )
    is_publication = models.BooleanField(
        verbose_name="Статус публикации", help_text="Укажите статус публикации", default=False
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="user",
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
    )

    class Meta:
        verbose_name = "Продкут"
        verbose_name_plural = "Продкуты"
        ordering = ["category", "name"]
        permissions = [
            ("can_unpublish_product", "Отмена публикации продукта"),
        ]

    def __str__(self):
        return f"{self.category}: {self.name} - {self.price}"
