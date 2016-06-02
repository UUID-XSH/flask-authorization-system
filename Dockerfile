FROM python:3.4

COPY . /data
RUN pip install -r /data/requirements.txt
EXPOSE 5000

ENTRYPOINT python /data/app.py