## Basic Command
- `django-admin startproject <project_name>` - Creates a new project.
- `python manage.py runserver` - Runs the server on the default port 8000.
- `python manage.py startapp <app_name>` - Creates a new app in the project.
- `python manage.py makemigrations [<app_name>]` - Creates migration files. If app_name is not provided, all apps are migrated.
- `python manage.py migrate` - Applies the migrations to the database.
- `python manage.py test` - Runs the tests in the tests.py file of the app.
- `python manage.py shell` - Opens the python shell with the django environment.
- `python manage.py createsuperuser` - Creates a superuser for the admin site.
- `python manage.py collectstatic` - Collects all the static files into the static folder.
