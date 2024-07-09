# Edit Views
The `generic.edit` module contains classes for modifying data. These classes are used to create, update, and delete objects.
The interact with forms and models to perform these actions.

## FormView
Form processing generally has 3 paths:
- Initial GET (blank or prepopulated form)
- POST with invalid data (typically redisplay form with errors)
- POST with valid data (process the data and typically redirect)
The example below shows how to handle forms with `FormView` class. The model instance is defined in the `form.instance` attribute.

```python
from  django.views.generic.edit import FormView

from .forms import MyForm

class MyFormView(FormView):
    form_class = MyForm
    template_name = 'my_template.html'
    success_url = '/success/'

    def form_valid(self, form):
        # Process the form data
        return super().form_valid(form)
```

## Model Form Views
Generic views will automatically create a `ModelForm`, so long as they can work out which model class to use.
The `model` attribute is used to specify the model to use for the form.
The `fields` attribute is used to specify the fields to include in the form.
If you specify both the `fields` and `form_class` attributes, an ImproperlyConfigured exception will be raised.
You should only specify one of these attributes.

The example below shows how to handle model forms with class based views.
```python
from django.views.generic.edit import CreateView, UpdateView

from .models import MyModel

class MyModelCreateView(CreateView):
    model = MyModel
    fields = ('field1', 'field2')
    template_name = 'my_template.html'
    success_url = '/success/' # can use get_absolute_url method if defined in the model
    # methods
    form_valid = None

class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['field1', 'field2']
    # form_class = MyModelForm # use this if you want to use a custom form class, no need to define fields
    template_name = 'my_template.html'
    success_url = '/success/'
```

### form_valid
All `FormView` based views have a `form_valid` method that is called when the form is valid.
This method is used to process the form data and can be overridden to add custom functionality.
Always call the super method before or after processing the form data.
```python
def form_valid(self, form):
    # Process the form data
    return super().form_valid(form)
```
