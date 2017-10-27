FROM python:3.5-slim-jessie

ENV FLASK_PROXY_PORT 8080

RUN apt-get update && apt-get install -y \
        gcc \
        libc-dev \
        libxslt-dev \
        libxml2-dev \
        libffi-dev \
        libssl-dev

RUN apt-cache search linux-headers-generic

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools six && pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /actionProxy
ADD actionproxy.py /actionProxy/

RUN mkdir -p /pythonAction
ADD pythonrunner.py /pythonAction/


CMD ["/bin/bash", "-c", "cd /pythonAction && python -u pythonrunner.py"]
