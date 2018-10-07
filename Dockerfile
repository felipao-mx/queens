FROM python:alpine3.7

COPY . /app

WORKDIR /app

RUN apk update && \
 apk add --no-cache bash && \
 apk add python3 postgresql-libs && \
 apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# RUN pip install -r requirements.txt

# CMD ["python", "./queens/app.py"]

# ENTRYPOINT [ "python", "./queens/app.py" ]