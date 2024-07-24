FROM python:3.11

COPY reqs.txt .

RUN pip install -r reqs.txt

WORKDIR src
