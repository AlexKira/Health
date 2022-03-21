FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE "mvp_project.settings.local"

COPY requirements.txt /usr/src/app/

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN mkdir -p /usr/src/app/logs/django

RUN apt-get update && apt-get install -y gettext libgettextpo-dev

RUN python3 manage.py collectstatic --noinput && \
    python3 manage.py makemessages

RUN python3 manage.py makemigrations && \
    python3 manage.py migrate

CMD python3 manage.py runserver 0.0.0.0:8000
