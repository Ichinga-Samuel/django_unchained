# Authentication with Django Rest Framework

## Default Authentication Setup

Use the following settings in settings.py to set up the default authentication scheme.
Sessions are used to power the Browsable API and the ability to log in and log out of it.
BasicAuthentication is used to pass the session ID in the HTTP headers for the API itself.

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # this is the default setting and does not need to be explicitly set
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

The default setting in Django REST Framework is actually a combination of Basic Authentication
and Session Authentication. Django’s traditional session-based authentication system is used
and the session ID is passed in the HTTP header on each request via Basic Authentication.
The advantage of this approach is that it is more secure since user credentials are only sent once,
not on every request/response cycle as in Basic Authentication. It is also more efficient since
the server does not have to verify the user’s credentials each time, it just matches the session ID
to the session object which is a fast look up.

## Token Authentication

Token-based authentication is stateless: once a client sends the initial user credentials to the
server, a unique token is generated and then stored by the client as either a cookie or in local
storage. This token is then passed in the header of each incoming HTTP request and the server
uses it to verify that a user is authenticated. The server itself does not keep a record of the user,
just whether a token is valid or not. The current best practice is to store tokens in a cookie with the
httpOnly and Secure cookie flags.

### Setup

Add the following to the settings.py file to enable token authentication and run the migrations.

```bash

```python
# settings.py
# add to installed apps
INSTALLED_APPS = [
    'rest_framework.authtoken',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

## Authentication Endpoints

### dj-rest-auth

```bash
pip install dj-rest-auth
```

Add the following to the installed apps in settings.py

```python
# settings.py
INSTALLED_APPS = [
    'dj_rest_auth',
    'dj_rest_auth.registration',  # for user registration
]
``` 

Add the following to the urls.py file

```python
# urls.py
from django.urls import path, include

urlpatterns = [
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
```

### Endpoints

Endpoints provided by `dj-rest-auth` are as follows:

* /registration
* /rest-auth/login
* /rest-auth/logout
* /rest-auth/password/reset
* /rest-auth/password/reset/confirm

## User Registration

Use `django-allauth` to handle user registration.

```bash
pip install django-allauth
```

Add the following to the installed apps in settings.py

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.sites',
    # 3rd party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # add this line
            ]
        }
    }
]
MIDDLEWARE = [
    ...,
    "allauth.account.middleware.AccountMiddleware",
]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SITE_ID = 1
```

## Authentication URLs

rest_framework.urls provides a set of URLs for the authentication views. These URLs are used for logging in and out of
the browsable API. The URLs are included by default in the browsable API.
If you're using the browsable API, you can log in and log out using the login and logout views.

```python
# urls.py
from django.urls import path

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]
```

## View Level Permissions

Permissions can be granted at view level also as shown below:

```python
# views.py
from rest_framework import permissions, generics


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
```

## Custom Permissions

Extend The Base Permission Class and override the `has_permission` and `has_object_permission` methods.

```python
from rest_framework import permissions


class IsAuthorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """Only authenticated users can view posts."""
        return request.user.is_authenticated

        def has_object_permission(self, request, view, obj):
            """Only the author of the post can edit it. But safe methods are allowed for all users."""
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.author == request.user
```
