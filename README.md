```
pip install django==3.1.4
django-admin startproject djcrm .
python3 manage.py runserver
python3 manage.py migrate
python3 manage.py startapp leads
python3 manage.py makemigrations
python3 manage.py shell 
python3 manage.py createsuperuser
```

`migrate` command that applies all the changes, that you have, to the database

`asgi.py` let us run Django server asynchronously

apps in django are the way to containerize certain aspects of the project

`apps.py` makes `leads` folder to be recognized as the app

`views.py` for handling web requests and returning responses as html pages or file or something else.

`makemigrations` creates a db schema according to our newly defined model

model managers - `<class_name>.objects` to access model's manager, which in turn
allows us to perform actions on the DB; `<class_name>.objects.create(**kwatgs)` to 
create a record in DB; `<class_name>.objects.all()`; `<class_name>.objects.filter(...)`
these commands return `queryset` object
