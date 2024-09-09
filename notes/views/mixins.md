# Mixins

Mixins are a form of multiple inheritance where behaviors and attributes of multiple parent classes can be
combined. They are used to add common functionality to class based views without repeating code.
A view should inherit from only one view class and one or more mixin classes. The two important mixins for working with
most views are the `ContextMixin` and `TemplateResponseMixin` classes.

### Template Response Mixin

The `TemplateResponseMixin` class is used to render a template.

```python
class TemplateResponseMixin:
    """A mixin that can be used to render a template."""
    # The Attributes and Methods provided can be overridden as needed,
    # Some attributes are not provided and must be implemented in the child classes

    # Attributes
    template_name = None
    template_engine = None
    response_class = TemplateResponse  # The class to use for the response
    content_type = None

    # Methods    
    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.

        Pass response_kwargs to the constructor of the response class.
        """

    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
```

#### Multiple Object Template Response Mixin

The `MultipleObjectTemplateResponseMixin` class is used to render a template with a list of objects.

```python
from django.views.generic.base import TemplateResponseMixin


class MultipleObjectTemplateResponseMixin(TemplateResponseMixin):
    """A mixin that can be used to render a template with a list of objects."""
    template_name_suffix = '_list'

    # The following methods are provide but can be overridden as needed
    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return a list. If the list is a queryset,
        we'll invent a template name based on the app and model name. This name gets put at the end of the template
        name list so that user-supplied names override the automatically generated ones.
        """

```

#### Single Object Template Response Mixin

The `SingleObjectTemplateResponseMixin` class is used to render a template with a single object.

```python
from django.views.generic.base import TemplateResponseMixin


class SingleObjectTemplateResponseMixin(TemplateResponseMixin):
    """A mixin that can be used to render a template with a single object."""
    template_name_field = None  # The field to use for the template name, if not provided, the model name is used
    template_name_suffix = "_detail"

    # The following methods are provide but can be overridden as needed
    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return a list. If the list is a queryset,
        we'll invent a template name based on the app and model name. This name gets put at the end of the template
        name list so that user-supplied names override the automatically generated ones.
        """
```

### Context Mixin

The `ContextMixin` class is used to add context data to the template.

```python

class ContextMixin:
    """A mixin that provides a way to set the context data for rendering the template."""
    extra_context = None  # Extra context data to add to the template

    # The following methods are provide but can be overridden as needed
    def get_context_data(self, **kwargs):
        """
        Return the context data to use for the template. Must return a dictionary. If extra_context is provided,
        it is added to the context data.
        Any subclass implementing this method should call super() to ensure all context data is included.
        """
```

#### Single Object Context Mixin

The `SingleObjectContextMixin` class is used to add a single object to the context data.

```python
class SingleObjectContextMixin(ContextMixin):
    """A mixin that provides a way to set the context data for a single object."""
    
    model = None  # The model to use
    queryset = None  # The queryset to use, if not provided, the model is used
    slug_field = "slug"  # The field to use for the slug
    context_object_name = None  # The context object name to use
    slug_url_kwarg = "slug"  # The slug keyword argument
    pk_url_kwarg = "pk"  # The pk keyword argument
    query_pk_and_slug = False  # Whether to query by pk and slug

    # The following methods are provide but can be overridden as needed
    def get_object(self):

        """
        Return the object the view is displaying. Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """

    def get_queryset(self):

        """Return the `QuerySet` that will be used to look up the object. This method is called by the default implementation
        of get_object() and may not be called if get_object() is overridden.
        """

    def get_slug_field(self):

        """Get the name of a slug field to be used to look up by slug."""

    def get_context_object_name(self, obj):

        """Get the name to use for the object."""

    def get_context_data(self, **kwargs):

        """Insert the single object into the context dict.""" 
```

#### Multiple Object Context Mixin

A mixin for views manipulating multiple objects.

```python
class MultipleObjectContextMixin(ContextMixin):
    """A mixin for views manipulating multiple objects."""
    allow_empty = True  # Whether to allow an empty queryset
    queryset = None  # The queryset to use
    model = None  # The model to use if queryset is not provided
    paginate_by = None  # The number of items to paginate by
    paginate_orphans = 0  # The number of orphans to allow
    context_object_name = None  # The context object name
    paginator_class = Paginator  # The paginator class to use

    # The following methods are provide but can be overridden as needed
    def get_queryset(self):

        """
        Return the list of items for this view. The return value must be an iterable and may be an instance of `QuerySet`
        in which case `QuerySet` specific behavior will be enabled.
        """

    def get_ordering(self):

        """Return the field or fields to use for ordering the queryset."""

    def paginate_queryset(self, queryset, page_size):

        """Paginate the queryset, if needed."""

    def get_paginate_by(self, queryset):

        """Get the number of items to paginate by, or ``None`` for no pagination."""

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True, **kwargs):

        """Return an instance of the paginator for this view."""

    def get_paginate_orphans(self):

        """Return the maximum number of orphans extend the last page by when paginating."""

    def get_allow_empty(self):

        """Return ``True`` if the view should display empty lists and ``False`` if a 404 should be raised instead."""

    def get_context_object_name(self, object_list):

        """Get the name of the item to be used in the context."""

    def get_context_data(self, *, object_list=None, **kwargs):

        """Get the context for this view."""
```

## Form Mixins

These mixins are used to handle forms in class based views.

### Form Mixin

Provide a way to show and handle a form in a request. It is the base class of the `ModelForm Mixin`

```python

class FormMixin:
    """A mixin that provides a way to show and handle a form in a request."""
    form_class = None  # The form class to use
    initial = {}  # The initial data to use for the form
    prefix = None  # The prefix to use for the form
    success_url = None  # The URL to redirect to after a successful form submission

    # The following methods are provide but can be overridden as needed
    def get_form_class(self):
    """Return the form class to use."""

    def get_initial(self):
    """Return the initial data to use for the form."""

    def get_prefix(self):
    """Return the prefix to use for the form."""

    def get_form_kwargs(self):
    """Return the keyword arguments for the form."""

    def get_form(self, form_class=None):
    """Return the form instance."""

    def get_success_url(self):
    """Return the URL to redirect to after a successful form submission."""

    def get_context_data(self, **kwargs):
    """Insert the form into the context dict."""

    def form_valid(self, form):
    """If the form is valid, redirect to the supplied URL."""

    def form_invalid(self, form):
    """If the form is invalid, render the invalid form."""
```
