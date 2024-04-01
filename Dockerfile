FROM python:3.9

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./req.txt .

RUN pip install -r req.txt

COPY . .

CMD ["gunicorn", "referal.referal.wsgi:application", "--log-level", "debug", "--workers", "6", "--timeout", "300", "--bind", "0:8000"]

