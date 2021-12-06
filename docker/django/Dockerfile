FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIPENV_CACHE_DIR=/web/app/pipenv_cache

WORKDIR /web/app

RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install --ignore-pipfile --deploy --system

COPY . .
