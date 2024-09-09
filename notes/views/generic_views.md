# Generic Views

Django’s generic views really shine when it comes to presenting views
of your database content. Because it’s such a common task, Django comes with a handful of built-in generic views
to help generate list and detail views of objects among other things.

## ListView

The ListView class is used to display a list of objects. It is a combination of `MultipleObjectMixin` and
`MultipleObjectTemplateResponseMixin`. A list view is used to display a list of objects.

```python
from django.views.generic import ListView

from .models import MyModel


class MyModelListView(ListView):
    model = MyModel
```

## DetailView

The DetailView class is used to display a detail view of an object. It is a combination of `SingleObjectMixin` and
`SingleObjectTemplateResponseMixin`.

```python
from django.views.generic import DetailView

from .models import MyModel


class MyModelDetailView(DetailView):
    model = MyModel
```

## Edit Views
Generic Edit views will automatically create a `ModelForm`, so long as they can work out which model class to use.
The `fields` attribute is used to specify the fields to include in the form.
The `CreateView`, `UpdateView`, and `DeleteView` classes rely on the `ModelFormMixin` class to create the form class.
The `ModelFormMixin` is a combination of `SingleObjectMixin` and `FormMixin`.

```python
