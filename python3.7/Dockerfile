FROM openwhisk/actionloop-python-v3.7:7cdff17

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools six && pip install --no-cache-dir -r requirements.txt
