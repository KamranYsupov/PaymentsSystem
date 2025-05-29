#  Запуск проекта

<h4>
1. Создайте файл .env в корневой директории 
проекта и установите переменные согласно .env.example:
</h4>

```requirements
PROJECT_NAME=
SECRET_KEY=
DEBUG=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_ROOT_PASSWORD=
DB_HOST=db
DB_PORT=3306
```

<h4>
2. Запустите docker compose:
</h4>

```commandline
docker compose up --build -d
```

<h4>
3. Создайте суперпользователя:
</h4>

```commandline
docker exec -it ${PROJECT_NAME}_web python manage.py createsuperuser
```

<h4>
4. Создайте организацию в админ-панели по адресу http://127.0.0.1:8000/admin 
</h4>


<br>

<h3>Эндпоинты:</h3>
* <b>Начисление баланса (POST):</b> http://127.0.0.1:8000/api/v1/webhook/bank/
* <b>Получение баланса организации (GET):</b> http://127.0.0.1:8000/api/v1/organizations/{inn}/balance/

