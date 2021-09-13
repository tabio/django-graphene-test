FROM python:3.8.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
     build-essential default-libmysqlclient-dev default-mysql-client

ADD requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


ENV PATH=$PATH:/root/.local/bin

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1


ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait


RUN mkdir /app
WORKDIR /app
ADD . /app/

CMD /wait && python manage.py runserver 0.0.0.0:8000
