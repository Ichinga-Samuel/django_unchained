# Bootstrap in django

## Use a Bootstrap CDN
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
 rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
 crossorigin="anonymous">
```

## Style Forms With Crispy Forms
```bash
pip install django-crispy-forms
pip install crispy-bootstrap5
```
Add them to the installed apps in `settings.py`
```python
INSTALLED_APPS = [
    ...,
    # Third Party Apps
    'crispy_forms',
    'crispy_bootstrap5',
]
# Add the following to the bottom of the file
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```
Render forms in the template
```html
{% load crispy_forms_tags %}
{{ form|crispy }}
```
