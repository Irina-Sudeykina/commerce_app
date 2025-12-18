# Проект "commerce_app" - электронная коммерция

## Описание:
 Проект "commerce_app" - это проект на Python, 
 простое веб-приложение магазина
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/commerce_app.git
 
 ```

 1. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

## Использование:
 
### Контроллер ProductListView(ListView) ###
Контроллер для рендера главной страницы

### Контроллер ProducDetailView(DetailView) ###
Контроллер для рендера страницы с товаром

### Контроллер ContactsView(View) ###
Контроллер для рендера страницы "Контакты"<br>
Осуществляет прием информаци с формы "Свяжитесь с нами":<br>
    - name - Имя<br>
    - phone - Телефон<br>
    - message - Сообщение<br>


### Контроллер BlogPostListView(ListView) ###
Контроллер для рендера главной блога

### Контроллер BlogPostDetailView(DetailView) ###
Контроллер для рендера поста блога

### Контроллер BlogPostCreateView(CreateView) ###
Контроллер для создания поста блога

### Контроллер BlogPostUpdateView(UpdateView) ###
Контроллер для редактирования поста блога

### Контроллер BlogPostDeleteView(DeleteView) ###
Контроллер для удаления поста блога


### Модель Product: ###
name - наименование,<br>
description - описание,<br>
image - изображение,<br>
category - категория,<br>
price - цена за покупку,<br>
created_at - дата создания,<br>
updated_at - дата последнего изменения.<br>


### Модель Category: ###
name - наименование,<br>
description - описание.<br>


### Модель BlogPost: ###
title - заголовок,<br>
description - содержимое,<br>
image - изображение,<br>
created_at - дата создания,<br>
is_publication - признак публикации,<br>
views_count - количество просмотров.<br>


## Загрузка фикстур: ###
Способ 1: - загрузка из файла<br>
Зайдите в Django shell и выполните:
```
Product.objects.all().delete()
Category.objects.all().delete()

BlogPost.objects.all().delete()
```
В терминале выполните:
```
python manage.py loaddata catalog_fixture.json --format json
python manage.py loaddata blogpost_fixture.json --format json
```
Способ 2 - используя кастомные команды<br>
В терминале выполните:
```
python manage.py add_products
python manage.py add_blogposts
```


## Запуск сервера:
В терминале выполните:
 ```
python manage.py runserver
 ```
Для остановки нажмите Ctrl + C

## Документация:

## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).
 