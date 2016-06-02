FROM python:3.4

ENV DB_URL
COPY . /data

ENTRYPOINT python /data/app.py