# CORS

Cross-Origin Resource Sharing (CORS)59 refers to the fact that whenever a client interacts with
an API hosted on a different domain (mysite.com vs yoursite.com) or port (localhost:3000 vs
localhost:8000) there are potential security issues.

## Django CORS Headers

Install *django-cors-header*.

```bash
 pip install django-cors-headers
```

## Setup

* add corsheaders to the INSTALLED_APPS
* add CorsMiddleware above CommonMiddleWare in MIDDLEWARE
* create a CORS_ALLOWED_ORIGINS config at the bottom of the file.

```python
# settings.py
INSTALLED_APPS = [
# 3rd party
...,
"corsheaders", # new
...
]

MIDDLEWARE = [
...,
"corsheaders.middleware.CorsMiddleware", # new
"django.middleware.common.CommonMiddleware",
..
]
CORS_ALLOWED_ORIGINS = (
"http://localhost:3000",
"http://localhost:8000",
)
```
