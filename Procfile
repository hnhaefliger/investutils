release: python utilities/manage.py makemigrations && python utilities/manage.py migrate --run-syncdb
web: gunicorn --pythonpath utilities utilities.wsgi
