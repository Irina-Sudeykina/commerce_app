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
 
### Контроллер home(request) ###
Контроллер для рендера главной страницы

### Контроллер contacts(request): ###
Контроллер для рендера страницы "Контакты"<br>
Осуществляет прием информаци с формы "Свяжитесь с нами":<br>
    - name - Имя<br>
    - phone - Телефон<br>
    - message - Сообщение<br>


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
description - описание,<br>


## Загрузка фикстуры: ###
Способ 1: - загрузка из файла<br>
Зайдите в Django shell и выполните:
```
Product.objects.all().delete()
Category.objects.all().delete()
```
В терминале выполните:
```
python manage.py loaddata catalog_fixture.json --format json
```
Способ 2 - используя кастомные команды<br>
В терминале выполните:
```
python manage.py add_products
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
 