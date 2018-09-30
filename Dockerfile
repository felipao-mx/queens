FROM python:alpine3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "./queens/app.py"]

ENTRYPOINT [ "python", "./queens/app.py" ]