FROM python:3.4

RUN pip install -r /data/requirements.txt

COPY . /data
EXPOSE 5000

ENTRYPOINT python /data/app.py