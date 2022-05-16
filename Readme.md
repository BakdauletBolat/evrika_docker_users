# Тестовое задание

Документация состоит из двух частей
- 1) Инструкция по установке Docker
- 2) Использование Сервер API 

## 1) Инструкция по установке Docker

## Установка

Клонирование проекта
```sh
git clone https://github.com/BakdauletBolat/evrika_docker_users.git
```

Поднять сервер с помощью docker-compose
```sh
docker-compose up --build
```

Создание необходимых миграций
```sh
docker-compose web exec python manage.py migrate
```

Создание учетная запись пользователя admin
```sh
docker-compose web exec python manage.py createsuperuser
```

Сервер запуститься на локальном сервере по адресу http://127.0.0.1/ 

## 2) Использование Сервер API 

Средства разработки: Python
Framework: Django
База данных: MySQL
Протокол: HTTP, порт 80

| URL | Краткое описание | Права |
| ------ | ------ |  ------ |
| http://127.0.0.1/api/users/sign-in/ | Авторизация | `user` |
| http://127.0.0.1/api/users/create/ | Добавление нового пользователя | `admin` |
| http://127.0.0.1/api/users/{id}/ | Получение информации о пользователе | `user` |
| http://127.0.0.1/api/users/{id}/update/ |Изменение статуса пользователя (Online, Offline) |  `admin` |
| http://127.0.0.1/api/users/ | Получение списка пользователей |  `user` |

## Авторизация 
---
```sh
http://127.0.0.1/api/users/sign-in/   METHOD "POST"
```

JWT авторизация для добавление нового пользователя и изменение статуса пользователя

#### Тело запроса (body)
Принимает 2 обязательных параметра `email` и `password`

Пример:

```sh
{
    "email": "admin@gmail.com",
    "password": 123
}
```

Ответом получаем `acsess` и `refresh` токены

Пример:

```sh
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2ODI5MDU3NCwiaWF0IjoxNjUyNzM4NTc0LCJqdGkiOiIxYTYxZWNlZTIxNWE0MzAwOTk2OGVlZGRmZmJkMzVkMyIsInVzZXJfaWQiOjF9.lQb9zEty15FcdUe_YABHUccPZjSlBbI_UOyROy6xst8"
    "acsess": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4MjkwNTc0LCJpYXQiOjE2NTI3Mzg1NzQsImp0aSI6ImQ4MDBhYjc0ZGQzZDQ4MjNiZmI0ZDViM2VkMTlhMmNhIiwidXNlcl9pZCI6MX0.uMy2BzAg34NzpRWaOC-yKgN8fjssRG-citV06Yewan8",
}
```

## Добавление нового пользователя
---
```sh
http://127.0.0.1/api/users/create/   METHOD "POST"
```

##### Добавить нового пользователя может только админ, поэтому для создание пользователя нужны права админа
---
#### Тело запроса (body)

Принимает 3 обязательных параметра `email`  `password` `username` 
Также 2 не обязательных параметра `phone` `status` 
`status` по умолчанию равно `Offline`

Пример:

```sh
{
    "email": "bakosh21345@gmail.com",
    "password": "secretkey",
    "username": "bakdaulet",
    "phone": "8777 777 77 77"
}
```

Ответом получаем `acsess` и `refresh` токены также уникальный `ID` нового пользователя

Пример:

```sh
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2ODI5MDU3NCwiaWF0IjoxNjUyNzM4NTc0LCJqdGkiOiIxYTYxZWNlZTIxNWE0MzAwOTk2OGVlZGRmZmJkMzVkMyIsInVzZXJfaWQiOjF9.lQb9zEty15FcdUe_YABHUccPZjSlBbI_UOyROy6xst8"
    "acsess": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4MjkwNTc0LCJpYXQiOjE2NTI3Mzg1NzQsImp0aSI6ImQ4MDBhYjc0ZGQzZDQ4MjNiZmI0ZDViM2VkMTlhMmNhIiwidXNlcl9pZCI6MX0.uMy2BzAg34NzpRWaOC-yKgN8fjssRG-citV06Yewan8",
    "user_id": 2
}
```

## Получение информации о пользователе
---
```sh
http://127.0.0.1/api/users/{id}/   METHOD "GET"
```

Для получение информации о пользователе передаем в адресном строке уникальный `id` 
Ответом получаем информацию о пользователе

#### Тело запроса (body)
Ничего не передаем

Ответом получаем информацию о пользователе

```sh
{
    "id": 2,
    "email": "bakosh21345@gmail.com",
    "status":"Offline",
    "phone": "8777 777 77 77",
    "username": "bakdaulet"
}
```

## Изменение статуса пользователя (Online, Offline)
---
```sh
http://127.0.0.1/api/users/{id}/update/   METHOD "PATCH" или "PUT"
```

Для изменение статуса пользователе передаем в адресном строке уникальный `id` 

#### Тело запроса (body)
Принимает 1 обязательный параметр `status`
- `status` может быть `Offline` или `Online`


Пример:

```sh
{
    "status":"Online"
}
```

Ответ от сервера:

```sh
{
    "id": 2,
    "status":"Status changed from Offline to Online"
}
```

## Получение списка всех пользователей
---
```sh
http://127.0.0.1/api/users/  METHOD "GET"
```
#### Тело запроса (body)
Ничего не передаем

Ответом получаем информацию массив пользователей

```sh
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "phone": null,
            "username": "admin",
            "email": "admin@gmail.com",
            "status": "Online"
        },
        {
            "id": 2,
            "phone": "8705555555",
            "username": "bakdaulet",
            "email": "bbb@gmail.com",
            "status": "Offline"
        }
    ]
}
```



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
