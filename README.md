# Profiles Rest API


Profiles Rest API


Create Python env
```
python -m venv ~/env
```

Activate the env
```
source ~/env/bin/activate
```

Install Python deps from requirements file
```
pip install -r requirements.txt
```

Create a django project
```
django-admin.py startproject profiles_project .
```

Add a App
```
python manage.py startapp profiles_api
```

Start the django App
```
python manage.py runserver 0.0.0.0:8000
```

Create a Migrations file for DB models
```
python manage.py makemigrations profiles_api
```

Run a migration
```
python manage.py migrate
```

Create a SuperUser
```
python manage.py createsuperuser
```