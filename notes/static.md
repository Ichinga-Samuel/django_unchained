# Static

Django’ s **STATICFILES_FINDERS** setting contains a list of finders that know how to discover static files from
various sources. Static files namespacing works similarly as template files namespacing, each app should have a static
folder with another folder inside with the app name for the static files. A static folder can also be created at the
project level point to it in the `STATICFILES_DIRS` variable of the settings.py file.

```python
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles" # new
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
```

Run `collectstatic` to move to the appropriate storage location as configured in `STATIC_ROOT`

```bash
python manage.py collectstatic
```