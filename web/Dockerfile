FROM python:3.5

RUN apt-get update
RUN apt-get install -y gettext
RUN apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
