FROM python:3.6.4-alpine3.6

COPY . .

RUN set -ex && pip install pipenv
RUN set -ex && pipenv install --deploy --system

EXPOSE 8000
CMD python manage.py runserver