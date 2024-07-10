# Views

A view is a callable which takes a request and returns a response. This can be more than just a function,
and Django provides an example of some classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins.

## Class Based Views

Class based views are a way to reuse code and structure views. They are more powerful than function based views.
Class based views use the `as_view()` method to return a view function for handling requests. The `as_view()` method
returns a callable that takes a request and returns a response.

```python
from django.views import View # The base class for all views

class MyView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')
```

## View

The base view class that all views inherit from. It does setup and initializes *request, args, and kwargs*

## Form Views

Class based views can be used to handle forms as shown in the example below.

```python
from django.views import View
from djang.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm

class MyFormView(View):
    # define the form class
    form = MyForm
    template_name = 'my_template.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            return HttpResponseRedirect('/success/')
        return render(request, 'my_template.html', {'form': form})
```

## Decorating a Class View

A class based view can be decorated using the `method_decorator` decorator. This is useful when you want to apply
decorators to all instances of a class based view.

```python
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class MyView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')
    
# you can also apply multiple decorators at once
@method_decorator([login_required, permission_required('myapp.permission')], name='dispatch')
class MyView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')
```

### Important Attributes of Class Based Views
- `request` : The request object
- `args` : The positional arguments passed to the view via the URL pattern
- `kwargs` : The keyword arguments passed to the view via the URL pattern
- `template_name` : The name of the template to render
