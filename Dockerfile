FROM python:3.12-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN pip install -r requirements.txt

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app