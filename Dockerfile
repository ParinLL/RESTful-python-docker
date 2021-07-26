FROM python:3.9.6-alpine3.14
LABEL maintainer=Parin_Lai
WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]