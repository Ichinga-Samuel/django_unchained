# Djang Restframework

## Installation

```bash
pip install djangorestframework
```

## Setup

Django REST Framework has a host of configurations that are namespaced inside a single Django setting called
REST_FRAMEWORK.
But first we add to local apps.

```python
# settings.py
# add to installed apps
INSTALLED_APPS = [
    rest_framework,

]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

```

## Views

Django REST Framework views are similar except the end result is serialized data in JSON format, not
the content for a web page! Django REST Framework views rely on a model, a URL, and a new
file called a serializer.

## Permissions

There are actually four built-in project-level permissions settings we can use:

* AllowAny `rest_framework.permissions.AllowAny` - any user, authenticated or not, has full access
* IsAuthenticated `rest_framework.permissions.IsAuthenticated` - only authenticated, registered users have access
* IsAdminUser `rest_framework.permissions.IsAdminUser` - only admins/superusers have access
* IsAuthenticatedOrReadOnly `rest_framework.permissions.IsAuthenticatedOrReadOnly` - unauthorized users can view any
  page, but only authenticated users have write, edit, or
  delete privilege
