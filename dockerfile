FROM python:latest
MAINTAINER FateGO
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn FateGO.wsgi:application --bind 0.0.0.0:8000 --workers 3