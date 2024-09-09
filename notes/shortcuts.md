<!-- toc -->
- [Django Shortcuts Functions](#django-shortcuts-functions)
- [render](#render)
- [redirect](#redirect)
- [get_object_or_404](#get_object_or_404)
<!-- /toc -->

# Django Shortcuts Functions

Django provides a number of shortcuts functions that can be used to perform common tasks.
These functions are located in the `django.shortcuts` module.

## render

The `render(request, template_name, context=None, content_type=None, status=None, using=None)`
function is used to render a template with a given context. The arguments are:

- `request`: The request object.
- `template_name`: The name of the template to render.
- `context`: A dictionary of values to pass to the template.
- `content_type`: The content type of the response, defaults to `text/html`.
- `status`: The HTTP status code to return, defaults to `200`.
- `using`: The name of the template engine to use, defaults to `None`.

```python
from django.shortcuts import render

def my_view(request):
    return render(request, 'my_template.html', {'name': 'John Doe'})
```

## redirect 

The `redirect(to, *args, permanent=False, **kwargs)` function is used to redirect to a given URL.
The arguments are:

- `to`: The URL to redirect to, this can be a model(get_absolute_url), view name(reverse), or relative or absolute url.
- `args`: Positional arguments to pass to the URL pattern.
- `permanent`: A boolean indicating whether the redirect is permanent, defaults to `False`.
- `kwargs`: Keyword arguments to pass to the URL pattern.

```python
from django.shortcuts import redirect

def my_view(request):
    return redirect('home')
```

## get_object_or_404

`get_object_or_404(klass, *args, **kwargs)` is a function that fetches an object from the database or raises
a 404 error if the object does not exist. The arguments are:

- `klass`: The model class to fetch the object from.
- `args`: Positional arguments to pass to the model manager's `get()` method.
- `kwargs`: Keyword arguments to pass to the model manager's `get()` method.

```python
from django.shortcuts import get_object_or_404

def my_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})
```

The async version of `get_object_or_404` is `aget_object_or_404`.
