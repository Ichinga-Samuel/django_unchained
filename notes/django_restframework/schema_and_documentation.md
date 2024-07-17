# Schema and Documentation

## Schema

The OpenAPI specification is the current default way to document an API. It describes common rules around format
for available endpoints, inputs, authentication methods, contact information, and more. As of this writing,
*drf-spectacular* is the recommended third-party package for generating an OpenAPI 3 schema for Django REST Framework.

### Setup

Install the package and add it to the installed apps in the settings.py file.

```bash
pip install drf-spectacular
```

```python
# settings.py
INSTALLED_APPS = [
    'drf_spectacular',
]

SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'My API description',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/api/v1/',
}

# add to rest_framework settings
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

### Generate Schema

Run the following command to generate the schema.

```bash
python manage.py spectacular --file schema.yml
```

### Dynamic Schema Generation

A more dynamic approach is to serve the schema directly from our API as a URL route. We’ll
do this by importing SpectacularAPIView and then adding a new URL path at api/schema/ to
display it.

```python
# urls.py
from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
```

## Documentation

A schema is well and good for consumption by a computer but humans generally prefer documentation for using an API.
There are two API documentation tools supported by drf-spectacular: Redoc and SwaggerUI.
Fortunately transforming our schema into either is a relatively painless process.

### Redoc

Redoc is a modern, open-source API documentation tool that generates beautiful API documentation from a schema.

#### Setup

Let’s begin with Redoc. To add it import SpectacularRedocView at the top of the _project/urls.py_
and then add a URL path at api/schema/redoc/.

```python
# urls.py
from drf_spectacular.views import SpectacularRedocView

urlpatterns = [
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

```

### SwaggerUI

SwaggerUI is another popular API documentation tool that generates interactive API documentation from a schema.

#### Setup

To add SwaggerUI, import SpectacularSwaggerView at the top of the _project/urls.py_ and then add a URL path at
api/schema/swagger/.

```python
# urls.py
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
```
