FROM openwhisk/python3action


COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash", "-c", "cd /pythonAction && python -u pythonrunner.py"]
