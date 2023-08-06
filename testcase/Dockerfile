FROM python:3.9.0-slim

RUN mkdir /app

COPY requirements.txt /app

RUN apt update && apt install -y gcc cmake libpq-dev python-dev
RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY .. /app

WORKDIR /app

CMD ["gunicorn", "testcase.wsgi:application", "--bind", "0:8000"]