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
Установите зависимости.
```
pip install -r requirements.txt
```
Загрузите тестовую базу данных
```
python backend/manage.py loaddata dump.json
```
Установите Node.js v11.13.0-x64
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
Запуск проекта на удаленном сервере выполняется средствами CI (GitHub Actions) и DockerHub.
Сделайте форк данного репозитория.
Скопируйте на удаленный сервер файлы docker-compose.yml и nginx.conf.
Пропишите в настройках GitHub Settings - Secrets - Actions - New repositorySecret секреты

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