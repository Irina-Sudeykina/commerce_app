import string

from django import forms
from django.core.exceptions import ValidationError

from blogs.models import BlogPost
from config.settings import PROHIBITED_WORDS


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-imput"
            else:
                field.widget.attrs["class"] = "form-control"


class BlogPostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ("views_count",)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        words_cleaned = [word.strip(string.punctuation).lower() for word in title.split()]

        set_a = set(words_cleaned)
        set_b = set(PROHIBITED_WORDS)

        common_words = set_a & set_b  # или set_a.intersection(set_b)

        if common_words:  # Если множество не пустое
            raise ValidationError("Заголовок поста не должен содержать запрещенных слов.")
        else:
            return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        words_cleaned = [word.strip(string.punctuation).lower() for word in description.split()]

        set_a = set(words_cleaned)
        set_b = set(PROHIBITED_WORDS)

        common_words = set_a & set_b  # или set_a.intersection(set_b)

        if common_words:  # Если множество не пустое
            raise ValidationError("Содержание поста не должно содержать запрещенных слов.")
        else:
            return description

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            # Проверка формата файла
            if not image.name.lower().endswith((".jpg", ".jpeg", ".png")):
                raise ValidationError("Поддерживаются только файлы форматов JPEG и PNG.")

            # Проверка размера файла
            if image.size > 5 * 1024 * 1024:  # 5 МБ
                raise ValidationError("Размер изображения не должен превышать 5 МБ.")

        return image
