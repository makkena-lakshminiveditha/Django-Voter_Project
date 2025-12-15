python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn Voter_Id.wsgi:application --bind 0.0.0.0:10000
