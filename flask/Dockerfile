FROM python:3.9.6-alpine3.14
LABEL maintainer=Parin_Lai
WORKDIR /app
COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    apk del .build-deps
COPY . .

ENTRYPOINT ["uwsgi", "app.ini"]