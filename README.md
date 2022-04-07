# API для YATUBE

Проект позволяет использовать функционал сервиса Yatube без посещения сайта. Реализована возможность просматривать, добавлять, редактировать и удалять посты, группы, комментарии, подписываться на авторов.

Полностью функционал доступен ***только аутентифицированному*** пользователю.

## Запуск проекта:

* Клонируем репозиторий:

git clone https://github.com/Helga61/api_final_yatube

* Открываем в командной строке проект:

cd api_final_yatube

* Cоздаем и активируем виртуальное окружение:

python -m venv venv
source venv/scripts/activate

* Устанавливаем зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

* Выполняем миграции:

python manage.py migrate

* Запускаем проект:

python manage.py runserver

[Полная документация и примеры запросов](http://127.0.0.1:8000/redoc/)
