# herokuデプロイ用

FROM python:3.8

COPY ./app /usr/src/app/

ADD requirements.txt /usr/src/app/requirements.txt
ADD startup.sh /usr/src/app/startup.sh
WORKDIR /usr/src/app/

RUN pip install -r requirements.txt && chmod +x ./startup.sh

CMD ["./startup.sh"]
