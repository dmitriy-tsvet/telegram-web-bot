# pull official base image
FROM python:3.10.7-slim-buster

# set work directory
WORKDIR /home/bot

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /home/bot/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /home/bot