FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gettext \
    mysql-client

RUN pip install -U pip

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
ADD requirements-dev.txt /code/
RUN pip install -r /code/requirements.txt -r /code/requirements-dev.txt --no-cache-dir

COPY . /code/
