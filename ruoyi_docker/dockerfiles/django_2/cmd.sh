cd /app/django_mall
python3 manage.py makemigrations
python3 manage.py migrate
cd /app
uwsgi --ini uwsgi.ini
