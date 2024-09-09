# Views

A view is a callable which takes a request and returns a response. This can be more than just a function,
and Django provides an example of some classes which can be used as views. These allow you to structure your views
and reuse code by harnessing inheritance and mixins.

## Function Based Views

Function based views are the simplest way to create views in Django. They are just Python functions that take a request
and return a response.

```python
from django.http import HttpResponse
from django.shortcuts import render


def my_view(request):
    return HttpResponse('Hello, World!')


def my_view_with_template(request):
    return render(request, 'my_template.html', {'name': 'John Doe'})


def my_view_with_args(request, name):
    return HttpResponse(f'Hello, {name}!')


def my_view_with_kwargs(request, *args, **kwargs):
    return HttpResponse(f'Hello, {kwargs["name"]}!')
```

## Decorating Function Based Views

Function based views can be decorated. Decorators are functions that modify the behavior of other functions.

### Allowed HTTP Methods

The decorators in django.views.decorators.http can be used to restrict access to views based on the request method.
These decorators will return a django.http.HttpResponseNotAllowed if the conditions are not met.

#### require_http_methods

The `require_http_methods` decorator takes a list of HTTP methods and only allows the view to be accessed by those methods.

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    return HttpResponse('Hello, World!')
```

#### require_safe()

The `require_safe` decorator only allows the view to be accessed by safe methods (GET, HEAD, OPTIONS).

# Class Based Views

At its core, a class-based view allows you to respond to different HTTP request methods with different class
instance methods, instead of with conditionally branching code inside a single view function. This allows you to
reuse code and structure views in a more organized way.

Class-based views have an `as_view()` class method which returns a function that can be called
when a request arrives for a URL matching the associated pattern. The `as_view()` method returns a function
that creates an instance of the class, calls `setup()` to initialize its attributes, and then calls its
`dispatch()` method. dispatch looks at the request to determine whether it is a **GET**, **POST**, etc,
and relays the request to a matching method if one is defined, or raises `HttpResponseNotAllowed` if not.

Class attributes are configured by setting them in the class definition or as keyword arguments to `as_view()`.

```python
# app/views.py

from django.http import HttpResponse
from django.views import View


class GreetingView(View):
    # set class attribute in class definition

    greeting = "Good Day"
    name = "John Doe"

    def get(self, request):
        return HttpResponse(f"{self.greeting} {self.name}")


# urls.py
from django.urls import path

from .views import GreetingView

# set attribute in as_view()
path('greet/', GreetingView.as_view(greeting="Morning Joe"))
```

## Using Mixins

Mixins are classes that provide methods that can be used in multiple classes. In django class based views they are used
to provide additional functionality to views. Django provides a number of mixins that can be used to extend the
functionality of class based views. Class based views can only inherit from one generic view - that is,
only one parent class may inherit from `View` and the rest (if any) should be mixins.

## Decorating Class Based Views

Class based views can be decorated.Since class based views aren’t functions, decorating them works differently
depending on if you’re using `as_view()` or creating a subclass. is used to apply decorators to specific methods
of a class based view.

```python
# app/urls.py
# decorating the as_view method. this works per instance of the class

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import AView

urlpatterns = [
    path('a/', login_required(AView.as_view())),
]
```

```python
# app/views.py

from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class AView(View):
    # decorating the dispatch method. this works for all instances of the class

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('Hello, World!')


# you can also apply the decorator to the class itself
@method_decorator(login_required, name='dispatch')
class AView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')
```

Apply multiple decorators at once. The decorators will process a request in the order they are passed to the decorator.
In the example, `never_cache()` will process the request before `login_required()`

```python
# a list of decorators
decorators = [never_cache, login_required]


# apply multiple decorators at once
@method_decorator(decorators, name="dispatch")
class ProtectedView(TemplateView):
    template_name = "secret.html"


# the same as above
@method_decorator(never_cache, name="dispatch")
@method_decorator(login_required, name="dispatch")
class ProtectedView(TemplateView):
    template_name = "secret.html"
```
> method_decorator passes *args and **kwargs as parameters to the decorated method on the class.
If your method does not accept a compatible set of parameters it will raise a TypeError exception.
