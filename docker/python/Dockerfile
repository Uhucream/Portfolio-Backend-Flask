FROM python:3.8

ADD requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000