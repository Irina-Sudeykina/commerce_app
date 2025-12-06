from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок поста")
    description = models.TextField(
        blank=True, null=True, verbose_name="Содержимое", help_text="Введите содержимое поста"
    )
    image = models.ImageField(
        upload_to="blogs/image", 
        blank=True, 
        null=True, 
        verbose_name="Изображение", 
        help_text="Загрузите изображение"
    )
    created_at = models.DateField(
        blank=True, auto_now_add=True, verbose_name="Дата создания", help_text="Укажите дату создания"
    )
    is_publication = models.BooleanField(
        default=True, verbose_name="Признак публикации", help_text="Укажите признак публикации"
    )
    views_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров", 
        help_text="Укажите количество просмотров", 
        default=0
    )

    class Meta:
        verbose_name = "Пост блога"
        verbose_name_plural = "Посты блога"
        ordering = [
            "created_at",
            "title",
        ]

    def __str__(self):
        return self.title
