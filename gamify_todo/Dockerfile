# base image
FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ADD . /code
