## Templates

#### Block Tag
```html
{% block content %} {% endblock content %}
```
#### url tag
```html
<a href="{% url 'view_name' %}">Tag</a>

<!--User app_name:view_name if name space is inuse-->
<a href="{% url 'app_name:view_name' %}">Tag</a>

```

#### Extending a template
```html
{% extends 'base.html' %}
```
