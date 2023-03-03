# Productlab_Test
___
The task consists of 2 parts:

1) Solution of logic task.
2) Creating webapp on Django 

## Web app
##### Description
The API recieves xlsx file with Wildberries's product articles (line by line in 1 column) or article value and returns product data in JSON format (article,brand,title).
##### Starting Instruction

1) You need to have installed Python and PostgreSQL.
2) Clone Git repo:
> $ git clone 
3) In directory with web app install venv, activate it and install all dependencies:
> $ python3 -m venv venv

> source venv/bin/activate

> $ pip install -r requirements.txt

4) Create postgres db using psql and grant all priveleges to created user:
> $ sudo -i -u postgres psql

> postgres=#CREATE DATABASE <dbname>;

> postgres=#CREATE USER <username> WITH PASSWORD '<password>';

> postgres=#GRANT ALL PRIVILEGES ON DATABASE <dbname> TO <username>;

5) Update **.env**  file in src/src with your data;

6) Migrate and makemigrations to db

> $ python manage.py makemigrations

> $ python manage.py migrate

7) Run server and test API (i use postman):
> python manage.py runserver

P.S. Работает только с товарами которые находятся **basket-05.wb.ru**