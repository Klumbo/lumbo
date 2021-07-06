FROM python:3.9.5

WORKDIR /home/

RUN echo "testing....."

RUN git clone https://github.com/Klumbo/lumbo.git

WORKDIR /home/lumbo/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=lumbo.settings.deploy && python manage.py migrate --settings=lumbo.settings.deploy && gunicorn lumbo.wsgi --env DJANGO_SETTINGS_MODULE=lumbo.settings.deploy --bind 0.0.0.0:8000"]