FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /recipes_project
WORKDIR /recipes_project
COPY ./recipes_project /recipes_project
COPY boot.sh .