FROM python:3.8.5

COPY djangovue /djangovue

COPY requirements.txt /djangovue/requirements.txt

WORKDIR /djangovue

RUN pip install -r requirements.txt && chmod 755 /djangovue/manage.py

CMD python manage.py runserver 0.0.0.0:8000