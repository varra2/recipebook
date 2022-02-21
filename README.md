# recipebook
Приложение для книги рецептов. Запускает сервер, доступный по адресу 127.0.0.1:8080
Для корректной работы приложения, требуется наличие программы docker 

Чтобы собрать приложение, нужно выполнить следующие шаги:

1. Поднять контейнер для базы данных:
* docker-compose up -d db
2. Применить миграции:
* docker-compose run app python manage.py migrate
3. Заполнить созданную базу данных примерами из фикстур:
* docker-compose run app python manage.py loaddata ingredient.json meal.json
4. Создать суперпользователя, чтобы иметь возможность изменять рецепты и добавлять свои:
* docker-compose run app python manage.py createsuperuser
5. Поднять контейнер для приложения:
 * docker-compose up -d app

Остановить работу контейнеров базы данных и приложения можно командой 
docker-compose stop
