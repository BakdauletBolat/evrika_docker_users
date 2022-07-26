# Тестовое задание

Документация состоит из 4 частей
- 1) Инструкция по установке Docker
- 2) Документация
- 3) Использование Сервер API 
- 4) Тесты

## 1) Инструкция по установке Docker

## Установка

Клонирование проекта
```sh
git clone https://github.com/BakdauletBolat/evrika_docker_users.git
```

Перейти в папку
```sh
cd evrika_docker_users
```

Сначало нужно поднять MySql базу данных и сервер 50-300секунд зависит от скорости интернета
```sh
docker-compose up --build
```

#### Для exec команд сервер должен быть включенным
---
Создание необходимых миграций
```sh
docker-compose exec web python manage.py migrate
```

Создать учетную запись пользователя admin
```sh
docker-compose exec web python manage.py createsuperuser
```

После миграций и создание учетного записа admin-(a) перезапускаем сервер (занимает 30 секунд)
```sh
docker-compose up
```

Сервер запуститься на локальном сервере по адресу http://127.0.0.1/ 



## 2) Документация в главном URL http://127.0.0.1


## 3) Использование Сервер API 

Средства разработки: Python
Framework: Django
База данных: MySQL
Протокол: HTTP, порт 80

| URL | Краткое описание | Права |
| ------ | ------ |  ------ |
| http://127.0.0.1/api/users/sign-in/ | Авторизация | `user` |
| http://127.0.0.1/api/users/create/ | Добавление нового пользователя | `admin` |
| http://127.0.0.1/api/users/{id}/ | Получение информации о пользователе | `user` |
| http://127.0.0.1/api/users/update/ |Изменение статуса пользователя (Online, Offline) |  `admin` |
| http://127.0.0.1/api/users/ | Получение списка пользователей |  `user` |
| http://127.0.0.1/api/todo/ | Получение списка постов |  `admin` |
| http://127.0.0.1/api/todo/create | Создание постов |  `admin` |
| http://127.0.0.1/api/todo/update | Обновление статуса постов |  `admin` |
| http://127.0.0.1/api/todo/{id} | Обновление статуса постов |  `admin` |
| http://127.0.0.1/api/todo/delete/{id} | Удаление постов |  `admin` |


### Все CRUD операций доступно в Postman по ссылке **[Посмотреть](https://www.postman.com/mission-observer-91554771/workspace/evrikausers/collection/15610246-c85daf6d-ad31-4c8c-ba28-fbe63249afeb?action=share&creator=15610246)**



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
  "data": {
      "type": "TokenObtainPairView",
      "attributes": {
          "password": "123",
           "email": "admin@gmail.com"
      }   
  }
}
```

Ответом получаем `acsess` и `refresh` токены

Пример:

```sh
{
    "data": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2ODQwODA3NSwiaWF0IjoxNjUyODU2MDc1LCJqdGkiOiI2YmY2YzUzNGYzYjY0N2FlYTk2YzNkYTg3ZTA1MTIxMCIsInVzZXJfaWQiOjF9.YxnlxAO8B9iNWzrhHP-vHIFrRcUD7YeK4EOhwj-TNGg",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NDA4MDc1LCJpYXQiOjE2NTI4NTYwNzUsImp0aSI6IjIyZjE0Y2RlYjAwMzQ0ZDlhOTM1ZGZmMzk0ZTM5N2QxIiwidXNlcl9pZCI6MX0.mNGt_r2ODbIt0j7GYNtDX_IvwJmHBV3S_wRTPlYPups"
    }
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

Принимает 3 обязательных атрибута `email`  `password` `username` 
Также 2 не обязательных атрибута `phone` `status` 
`status` по умолчанию равно `Offline`

Пример:

```sh
{
  "data": {
      "type": "User",
      "attributes": {
        "username": "bakdaulet",
        "email": "asasdaadasdsaasdsddddd@daasdasddasаgmail.com",
        "password": "123"
      }   
  }
}
```

Ответом получаем `acsess` и `refresh` токены также уникальный `ID` нового пользователя

Пример:

```sh
{
    "data": {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NDA3OTgyLCJpYXQiOjE2NTI4NTU5ODIsImp0aSI6IjgyOWExYWE1NTIzYTQyNDg4MzYyZTE1YjY3N2Q3Y2QxIiwidXNlcl9pZCI6MzZ9.7gDnWTbdOFWOeyCTl8iKDNJLzOENGIzNwtxL7rylWKU",
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2ODQwNzk4MiwiaWF0IjoxNjUyODU1OTgyLCJqdGkiOiIwZDhhMDA3OGY3ODY0NThhOWM5NDA1YTYxMzBmZmI4MSIsInVzZXJfaWQiOjM2fQ.pBKYeUX2-G7yGqOWHFk5cUvIoOWP0qBirIT8BTGPom0",
        "id": 36
    }
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
    "data": {
        "type": "User",
        "id": "3",
        "attributes": {
            "phone": null,
            "username": "b2",
            "email": "admin3@gmail.com",
            "status": "Offline"
        }
    }
}
```

## Изменение статуса пользователя (Online, Offline)
---
```sh
http://127.0.0.1/api/users/update/   METHOD "PATCH" или "PUT"
```

#### Тело запроса (body)
Для изменение статуса пользователе передаем `id` 
Принимает 1 обязательный параметр `status`
- `status` может быть `Offline` или `Online`


Пример:

```sh
{
    "data": {
        "type": "User",
        "id": 3,
        "attributes": {
            "status": "Offline"
        }
    }
}
```

Ответ от сервера:

```sh
{
    "data": {
        "type": "User",
        "id": "3",
        "attributes": {
            "status": "Status changed from Offline to Offline"
        }
    }
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
    "links": {
        "first": "http://127.0.0.1:8000/api/users/?page%5Bnumber%5D=1",
        "last": "http://127.0.0.1:8000/api/users/?page%5Bnumber%5D=4",
        "next": "http://127.0.0.1:8000/api/users/?page%5Bnumber%5D=2",
        "prev": null
    },
    "data": [
        {
            "type": "User",
            "id": "1",
            "attributes": {
                "phone": null,
                "username": "bakdaulet",
                "email": "admin@gmail.com",
                "status": "Online"
            }
        },
        {
            "type": "User",
            "id": "2",
            "attributes": {
                "phone": null,
                "username": "bakdaulet",
                "email": "bakdaulet@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "3",
            "attributes": {
                "phone": null,
                "username": "b2",
                "email": "admin3@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "4",
            "attributes": {
                "phone": null,
                "username": "b2",
                "email": "admin2@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "5",
            "attributes": {
                "phone": null,
                "username": "bakdaulet",
                "email": "bakdaulet2@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "6",
            "attributes": {
                "phone": null,
                "username": "bakdaulet",
                "email": "bakdaulet3@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "7",
            "attributes": {
                "phone": null,
                "username": "bakdaulet",
                "email": "bakdaulet4@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "8",
            "attributes": {
                "phone": null,
                "username": "bakdaulet",
                "email": "bakdaulet5@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "9",
            "attributes": {
                "phone": null,
                "username": "bakdaulet",
                "email": "bakdaulet7@gmail.com",
                "status": "Offline"
            }
        },
        {
            "type": "User",
            "id": "10",
            "attributes": {
                "phone": null,
                "username": "bbb",
                "email": "bakasda@gmail.com",
                "status": "Offline"
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 4,
            "count": 34
        }
    }
}
```

###  4) Для теста запускаем команду
```sh
docker-compose exec web python manage.py test
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
