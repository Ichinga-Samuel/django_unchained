# Mixins
Mixins are a form of multiple inheritance where behaviors and attributes of multiple parent classes can be
combined. They are used to add common functionality to class based views without repeating code. A view should inherit from
only one view class and one or more mixin classes.

## Context and Template Mixins
Two central mixins are provided that help in providing a consistent interface to working with templates in
class-based views.

### Template Response Mixin
The `TemplateResponseMixin` class is used to render a template. It is a mixin class that can be used with any view class.
It uses the `render_to_response` method to render the template. All views that render a template should inherit from this class.
```python
class TemplateResponseMixin:
    """A mixin that can be used to render a template."""
    template_name = None
    template_engine = None
    response_class = TemplateResponse
    content_type = None
    
    # The following methods are provide but can be overridden as needed
    get_template_names = None # Returns the template names to use
    render_to_response = None # Renders the template with the context data and returns a response
```

### Context Mixin
The `ContextMixin` class is used to add context data to the template. It is a mixin class that can be used with any view class.
It provides the `get_context_data` method to add extra context data to the template. When using this method, always call the
super method before or after adding extra context.
The `extra_context` attribute is used to add extra context data to the template without modifying the `get_context_data` method.

## Object Mixins
This section covers mixins that are used to provide objects to views. They are used to provide a list of objects or a single object.
The `SingleObjectMixin` and `MultipleObjectMixin` classes are used to provide a single object and a list of objects respectively.
They both inherit from the `ContextMixin` class.

### Single Object Mixins
The `SingleObjectMixin` class is used to provide a single object to a view. It uses the `get_object` method to obtain the object
to display. It is best used with views that display a single object in combination with the appropriate view class.
It looks for pk and slug keyword arguments as declared in the URLConf, and uses them to query the database for the object to display.
```python
class SingleObjectMixin(ContextMixin):
    """
    Provide the ability to retrieve a single object for further manipulation.
    """
    model = None
    queryset = None
    slug_field = "slug"
    context_object_name = None
    slug_url_kwarg = "slug"
    pk_url_kwarg = "pk"
    query_pk_and_slug = False
    
    # The following methods are provide but can be overridden as needed
    get_object = None # Returns the object to display
    get_queryset = None # Returns the queryset to use, custom filtering can be done here
    get_slug_field = None
    get_context_object_name = None # Returns the context object name
    get_context_data = None # Returns the context data
```

### Multiple Object Mixins
The `MultipleObjectMixin` class is used to provide a list of objects to a view. It uses the `get_queryset` method to obtain the
queryset to display. It is best used with views that display a list of objects in combination with the appropriate view class.
```python
class MultipleObjectMixin(ContextMixin):
    """A mixin for views manipulating multiple objects."""
    allow_empty = True
    queryset = None
    model = None
    paginate_by = None
    paginate_orphans = 0
    context_object_name = None
    paginator_class = Paginator
    page_kwarg = "page"
    ordering = None
    
    # The following methods are provide but can be overridden as needed
    get_queryset = None # Returns the queryset to use, custom filtering can be done here
    get_ordering = None # Returns the ordering to use
    get_paginate_by = None # Returns the number of items to paginate by
    get_paginate_queryset = None # Paginates the queryset
    get_paginator = None # Returns the paginator
    get_paginate_orphans = None # Returns the number of orphans
    get_allow_empty = None # Returns whether to allow an empty queryset
    get_context_object_name = None # Returns the context object name
    get_context_data = None # Returns the context data
```

## Form Mixins 
These mixins are used to handle forms in class based views.

### Form Mixin
The `FormMixin` class is used to handle forms in class based views. The are the base class for `FormModelMixin`.

```python
"""Provide a way to show and handle a form in a request."""
    initial = {}
    form_class = None
    success_url = None
    prefix = None

    # The following methods are provide but can be overridden as needed
    get_form_class(self) = # Returns the form class to use
    get_initial(self) # Returns the initial data to use for the form
    get_prefix(self) # Returns the prefix to use for the form
    get_form_kwargs(self) # Returns the keyword arguments for the form
    get_form(self, form_class=None) # Returns the form instance
    get_success_url(self) # Returns the URL to redirect to after a successful form submission
    get_context_data(self, **kwargs) # Returns the context data
    form_valid(self, form) # Handles a valid form
    form_invalid(self, form) # Handles an invalid form
```
## Authentication Mixins
These mixins are used to require that a user be logged in or pass a test to access a view. They are used to restrict access to views
based on the user's authentication status or other criteria. The inherit from a base `AccessMixin` class.
### Login Required Mixin
The `LoginRequiredMixin` class is used to require that a user be logged in to access a view. It is a mixin class that can be
used with any view class.
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin):
    login_url = None # uses the LOGIN_URL setting by default
    permission_denied_message = ""
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME
```

### User Passes Test Mixin
The `UserPassesTestMixin` class is used to require that a user passes a test to access a view. It is a mixin class that can be
used with any view class. The `test_func` method should be overridden to return a boolean value.

```python
from django.contrib.auth.mixins import UserPassesTestMixin

class MyView(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
```
