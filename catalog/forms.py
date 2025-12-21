from django import forms
from .models import Product
from config.settings import PROHIBITED_WORDS
from django.core.exceptions import ValidationError

import string
import os


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-imput'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('views_count',)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        words_cleaned = [word.strip(string.punctuation).lower() for word in name.split()]
        
        set_a = set(words_cleaned)
        set_b = set(PROHIBITED_WORDS)

        common_words = set_a & set_b # или set_a.intersection(set_b)

        if common_words: # Если множество не пустое
            raise ValidationError('Наименование продукта не должно содержать запрещенных слов.')
        else:
            return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        words_cleaned = [word.strip(string.punctuation).lower() for word in description.split()]
        
        set_a = set(words_cleaned)
        set_b = set(PROHIBITED_WORDS)

        common_words = set_a & set_b # или set_a.intersection(set_b)

        if common_words: # Если множество не пустое
            raise ValidationError('Описание продукта не должно содержать запрещенных слов.')
        else:
            return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной.')
        else:
            return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Проверка формата файла
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('Поддерживаются только файлы форматов JPEG и PNG.')

            # Проверка размера файла
            if image.size > 5 * 1024 * 1024:  # 5 МБ
                raise ValidationError('Размер изображения не должен превышать 5 МБ.')

        return image
