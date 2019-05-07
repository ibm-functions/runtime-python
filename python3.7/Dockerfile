FROM openwhisk/actionloop-python-v3.7:aaeb2ff

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools six && pip install --no-cache-dir -r requirements.txt
