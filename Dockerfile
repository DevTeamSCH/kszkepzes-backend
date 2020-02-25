# pull official base image
FROM python:3.8.1

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev python-django-extensions postgresql-client netcat
RUN pip install --upgrade pip
COPY ./requirements/production.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

RUN apt-get -y update && apt-get -y autoremove

# copy entrypoint.sh
COPY ./src/entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY ./src /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]