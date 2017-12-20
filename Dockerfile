FROM python:3.6

# Setup Python Environment
RUN apt-get update

WORKDIR /axds/

COPY requirements.txt ./


RUN apt-get install -y curl build-essential

RUN pip install -r requirements.txt

CMD ./manage.py migrate && ./manage.py runserver 0.0.0.0:8000
