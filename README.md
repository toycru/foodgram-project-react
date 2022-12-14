# Foodgram
[![example event parameter](https://github.com/toycru/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/toycru/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

Foodgram или «Продуктовый помощник» - это онлайн-сервис, на котором пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.


## Использованные технологии
- Python 3.7
- Django 2.2.19
- Django REST framework 3.13
- PostgreSQL 13.0
- NGINX 1.19
- Gunicorn 20.1
- GitHub Actions


## Тестовый сайт проекта
Проверить функционал проекта можно на сайте: http://158.160.9.165/
Тестовый логин: `test@ya.ru`
Пароль: `qwerty` 

![Скриншот тестового сайта проекта](https://github.com/toycru/foodgram-project-react/foodgram_screen.jpg)

## Установка и запуск проекта на локальном компьютере:
Клонируйте репозиторий на локальную машину.
```
git clone <адрес репозитария>
```
Установите виртуальное окружение.
```
python -m venv venv
```
Активируйте виртуальное окружение.
```
source venv\Scripts\activate
```
Перейти в директорию /infra и создать файл .env:
```
cd infra
touch .env
```
Заполните файл содержанием из файла в примере [infra/.env.example](https://github.com/toycru/foodgram-project-react/blob/master/infra/.env.example):
```
DB_ENGINE='django.db.backends.postgresql' # указываем, что работаем с postgresql
DB_NAME='postgres' # имя базы данных
POSTGRES_USER='postgres' # логин для подключения к базе данных
POSTGRES_PASSWORD='postgres' # пароль для подключения к БД (установите свой)
DB_HOST='127.0.0.1' # название сервиса (контейнера)
DB_PORT='5432' # порт для подключения к БД
SECRET_KEY = <секретный ключ из одноименного параметра>
```
Перейдите в каталог `backend`. Установите зависимости.
```
cd ../backend
pip install -r requirements.txt
```
**Опционально**:
- Либо загрузите тестовую базу данных (при необходимости)
```
python backend/manage.py loaddata dump.json
```
- Либо (для работы с "пустым" проектом) создайте суперпользователя
```
python manage.py createsuperuser
```
и импортируйте ингредиенты: 
```
python manage.py import_ingredients
```
Соберите статику:
```
python manage.py collectstatic
```
Для запуска фронтенда установите Node.js v11.13.0-x64
Перейдите в каталог фронтенда и запустите NPM
```
cd frontend/
npm install
npm start
```
Запустите локальный сервер.
```
python backend/manage.py runserver
```

## Запуск проекта на удаленном сервере
Запуск проекта на удаленном сервере выполняется средствами контейнеров Docker.
Перейдите на удаленный сервер.
Установите Docker и Docker-compose.
Создайте или скопируйте на сервер конфигурационные файлы `docker-compose.yml` и `nginx.conf` из каталога `infra/`
Запустите docker compose:
```
sudo docker-compose up
```
После сборки docker-compose создадутся три контейнера:
- контейнер базы данных db
- контейнер приложения backend
- контейнер веб-сервера nginx
Создайте миграции в контейнере приложения `backend`
```
sudo docker-compose exec backend python manage.py makemigrations users
sudo docker-compose exec backend python manage.py migrate
sudo docker-compose exec backend python manage.py makemigrations recipes
sudo docker-compose exec backend python manage.py migrate
```
**Опционально**:
- Либо загрузите тестовую базу данных (при необходимости)
```
sudo docker-compose exec backend python backend/manage.py loaddata dump.json
```
- Либо (для работы с "пустым" проектом) создайте суперпользователя
```
sudo docker-compose exec backend python manage.py createsuperuser
```
и импортируйте ингредиенты: 
```
sudo docker-compose exec backend python manage.py import_ingredients
```
Соберите статику:
```
sudo docker-compose exec backend python manage.py collectstatic
```


## Эндпоинты сервисов
Описание всех запросов и полей можно найти в документации API сервиса
В каталоге infra
```
cd infra
```
выполните команду 
```
docker-compose up
```
Тогда по адресу http://localhost/api/docs/ будет доступна спецификация проекта.

**Авторы проекта** 
[Дмитрий ToyCru](https://github.com/toycru) - бэкенд 
[Команда Яндекс.Практикума](https://github.com/yandex-praktikum/foodgram-project-react) - фронтенд