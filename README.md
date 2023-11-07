# TestCase with Docker
## Стек технологий: Python 3, Django REST Framework, PostgreSQL, Docker, Celery, Redis
____
##### Создание файла с переменными окружения .env
Пример:
- выбор движка СУБД ```DB_ENGINE=django.db.backends.postgresql```
- название базы ```DB_NAME=postgres```
- имя пользователя базы ```POSTGRES_USER=postgres```
- пароль базы данных ```POSTGRES_PASSWORD=postgres```
- адрес базы ```DB_HOST=db``` 
- порт базы```DB_PORT=5432```
dfgdfgdfg

### Запуск приложения:
```docker-compose up```

### Выполнить миграции:
```docker-compose exec web python manage.py makemigrations``` \
```docker-compose exec web python manage.py migrate``` 

### Создать суперпользователя для windows/linux (winpty or sudo в начале) :
```docker-compose exec web python manage.py createsuperuser```

### Запуск сервера
```sudo docker-compose exec web python manage.py runserver```

### Запуск celery для отправки сообщений
```sudo docker-compose exec celery celery -A testcase beat```

### Информация об авторе проекта
```Ivan Morozov```

