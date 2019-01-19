FROM python:3.4
MAINTAINER ciller@localhost

copy ./budgetproject /budgetproject

WORKDIR /budgetproject

RUN pip install -r requirements.txt 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]