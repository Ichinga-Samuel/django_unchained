# Generic Views
Django’s generic views really shine when it comes to presenting views
of your database content. Because it’ s such a common task, Django comes with a handful of built-in generic
views to help generate list and detail views of objects

## Common Generic Views
### ListView
The ListView class is used to display a list of objects. It is a combination of `MultipleObjectMixin` and
`MultipleObjectTemplateResponseMixin`.
```python
from django.views.generic import ListView
from .models import MyModel

class MyModelListView(ListView):
    template_name_suffix = "_list" # The template to use
```

### DetailView
The DetailView class is used to display a detail view of an object. It is a combination of `SingleObjectMixin` and 
`SingleObjectTemplateResponseMixin`.

## Important Methods

### get_context_data
The `get_context_data` method is used to add extra context to the template. It returns a dictionary of context data.
Always call the super method before or after adding extra context as the need may be. It is provided by the `ContextMixin` class.
```python
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['extra_context'] = 'Extra Context'
    return context
```

### get_queryset
The `get_queryset` method is used to dynamically obtain the queryset. It returns the queryset to use for the view.
It is provided by both the `MultipleObjectMixin` and `SingleObjectMixin` classes.
```python
def get_queryset(self):
    return MyModel.objects.filter(active=True)
```

### get_object
The `get_object` method is used to dynamically obtain the object to display. It returns the object to display and 
allows for custom actions to be performed. It is provided by the `SingleObjectMixin` class.
```python
def get_object(self):
    return MyModel.objects.get(pk=self.kwargs['pk'])
```
