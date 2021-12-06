web: gunicorn --pythonpath develops_today develops_today.wsgi
worker: sh -c 'cd develops_today && celery -A develops_today worker --beat -l INFO --pool=solo'
