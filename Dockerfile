# herokuデプロイ用

FROM python:3.8

COPY ./app /usr/src/app/

ADD requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app/

RUN pip install -r requirements.txt

CMD ["./init_db.sh", "flask", "db", "migrate", "flask", "db", "upgrade", "gunicorn", "-c", "gunicorn_settings.py", "application:app"]
