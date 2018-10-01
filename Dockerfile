FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
ADD requirements-dev.txt /code/
RUN pip install -r /code/requirements.txt -r /code/requirements-dev.txt --no-cache-dir

COPY . /code/
