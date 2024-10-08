# Welcome to Django

Django is a high-level web framework written in Python that encourages rapid development and clean, pragmatic design.

## Starting a Project

```shell
django-admin startproject <project_name> [folder_name]
```

Creates a project inside the folder with the given name. The folder name is optional, if not provided,
the project is created in the current directory and the project name is used as the folder name.

### Run the Server

Start the server from inside the project directory

```shell
python manage.py runserver  # Runs the server on the default port 8000
```

### Run Migrations

Migration files are used to propagate changes you make to your models (adding a field, deleting a model, etc.) into your
database schema. Django tracks the changes you make to your models and stores them as migration files.

```shell
python manage.py makemigrations [app_name] # Creates migration files. If app_name is not provided, all apps are migrated.
python manage.py migrate
```

## Dango Project Structure

The django version of **MVC** is **MVTU**. It stands for **Model**, **View**, **Template**, **URL**.
Django organises a project into apps. Each app has its own models, views, templates and urls.

### Starting an App

```shell
python manage.py startapp <app_name>
```

After creating an app add it to the installed app array in the settings.py file.

```python
# settings.py
INSTALLED_APPS = [
    ...
    # local apps
    'app_name.apps.AppNameConfig',
]
```

### Views

Views are the functions that handle requests and return responses. Within an app, views are defined in the
views.py file. Each view is a function that takes a request object and returns a response object.

```python
# app/views.py
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, World!")


# Using the render function to render a template
def home_template(request, name):
    # name argument comes from the URL
    return render(request, 'home.html', {'name': name})


def my_view(request, *args, **kwargs):
    # args and kwargs are optional and are captured from the URL
    return HttpResponse("Hello, World!")
```

### URLConf

Each app may have a urls.py file that maps URLs to views provided by the app. The urlpatterns is a list of path
instances. Each path() instance maps a URL pattern to a view. The `path()` function takes three arguments:
_route_ as a string or regex, _view_ as function or class method, _kwargs_, and, optional _name_ and _pattern_
arguments as the case maybe. To namespace an app, you can set the _app_name_ variable in the _urls.py_ file of the app.

```python
# app/urls.py

from django.urls import path
from .views import HomeView

app_name = 'app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # use angle brackets to capture a variable from the URL. The variable is passed to the view function.
    path('welcome/<name>/', HomeView.as_view(), name='home')
]
```

The project level _urls.py_ file combines the urls of all the apps in the project. It is the main URL configuration
file, and, should be in the folder containing the settings.py file .i.e. the project folder. It uses the `include()`
function to include the urls of all apps apart from the admin app.

```python
# project/urls.py

from django.urls import path, include
from django.contrib import admin

# assuming the app is named app
urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
]
```

### Templates

Templates are used to generate HTML dynamically. They are stored in the templates folder of the app.
Inside the templates folder another folder with the app name is created to store the templates. Alternatively, the
templates can be stored in the templates folder of the project. Point to it in the TEMPLATES variable of _settings.py_
file.

```python
# settings.py

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
    },
]
```

### Models

A model is the single, definitive source of information about your data. It contains the essential fields and
behaviors of the data you are storing. Django follows the **DRY** Principle. The goal is to define your data model in
one place and automatically derive things from it. Models are defined in the models.py file of the app.
Each model is a class that inherits from the django.db.models.Model class. The attributes of the class instance
represent the
fields of the model. The model class is used to create the database schema.

```python
# app/models.py

from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

After defining the model, create the migration files and apply them to the database.

```shell
python manage.py makemigrations [app_name] # Creates migration files. If app_name is not provided, all apps are migrated.
python manage.py migrate # Applies the migrations to the database.
```

### Admin

Django provides an admin interface that can be used to manage the database.
To use the admin interface, register the models in the _admin.py_ file of the app.
Create Superuser to access the admin interface.

```python
# app/admin.py

from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
```

create a superuser to access the admin interface, run the command below and follow the prompts

```shell
python manage.py createsuperuser 
```

### Testing

Tests are routines that check the operation of your code. Django has a test framework that can be used to test the apps.
The tests are written in the tests.py file of the app.

```shell
# Run the tests
python manage.py test

# Test an app
python manage.py test <app_name>
```
