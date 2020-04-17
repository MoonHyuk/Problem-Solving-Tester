FROM python:3.8-alpine

RUN apk update && apk add php7

WORKDIR /src/ps/
COPY tester.py .

CMD python tester.py