#!/bin/sh

# Создание папки 'media', если она не существует
mkdir -p /my_app_directory/media/booking

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3 manage.py flush --no-input
python3 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'saiwa@mail.ru', '1')" | python manage.py shell

exec "$@"