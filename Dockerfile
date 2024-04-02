FROM python:3.9

RUN apt-get update -y
RUN apt-get upgrade -y

COPY . .

RUN pip install -r req.txt

WORKDIR pattern/

# RUN python3 manage.py migrate

CMD ["gunicorn", "referal.wsgi:application", "--log-level", "debug", "--workers", "6", "--timeout", "300", "--bind", "0:8000"]

