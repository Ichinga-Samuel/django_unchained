<!-- toc -->
* [Django Form Class](#django-form-class)
* [Creating a Form.](#creating-a-form)
* [Working with Form Templates](#working-with-form-templates)
  * [Form Rendering](#form-rendering)
  * [Reusable field group templates](#reusable-field-group-templates)
  * [Form Field Attributes](#form-field-attributes)
* [Model Form](#model-form)
  * [Saving a ModelForm](#saving-a-modelform)
  * [Selecting Fields to Use](#selecting-fields-to-use)
  * [Overriding and Customizing the Default Fields](#overriding-and-customizing-the-default-fields)
    * [Customizing the Form Field](#customizing-the-form-field)
    * [Validating Form Data on Multiple Fields](#validating-form-data-on-multiple-fields)
* [Form Api](forms_api.md)
<!-- /toc -->

# Django Form Class

Form class describes a form and determines how it works and appears. Django provides a number of built-in form
classes that can be used to quickly create forms. These classes are located in the `django.forms` module.

## Creating a Form.

To create a form, you need to create a class that inherits from `django.forms.Form` or `django.forms.ModelForm`.

```python
# app/forms.py
from django import forms


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)  # max_length is a validation constraint will apply in html
    # nonvalidate will not apply validation constraint in html
    email = forms.EmailField(label='E-Mail', nonvalidate=False)  # custom label will be used in the form label. 
    message = forms.CharField(widget=forms.Textarea)  # custom widget will be used in the form


# app/views.py
from django.shortcuts import render

from .forms import MyForm


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
```

```html
<!-- app/templates/my_template.html -->
<!-- form rendering -->
<!-- the surrounding form tag is not included in the form class -->
<form method="post" action="/myform/">
  {% csrf_token %}
  <input type="text" name="name" id="name" maxlength="100" required>
  <input type="email" name="email" id="email" required>
  <textarea name="message" id="message" required></textarea>
  <button type="submit">Submit</button>
</form>
```

A Form instance has an `is_valid()` method, which runs validation routines for all its fields if all fields are valid
it returns `True` and populates the `cleaned_data` attribute, which is a dictionary of validated form data.
Access to unvalidated data is still possible directly from `request.POST`.
A form can be _bound_ or _unbound_. A bound form has data associated with it, while an unbound form does not.
The form is bound when it is instantiated with data, as in `form = MyForm(request.POST)`. The `is_bound` attribute
can be used to check if the form is bound or not.

## Working with Form Templates

Django provides a number of template tags and filters to work with forms. These tags and filters are located in the
`django.forms` module.

### Form Rendering

The default template can be customized by setting field_template_name in your project-level `FORM_RENDERER` setting
or on a single field.

```python
class MyForm(forms.Form):
    subject = forms.CharField(template_name="my_custom_template.html")
```

### Reusable field group templates

Each field is an attribute of the form, using `{{ form.name_of_field }}` in a template. A field has
an `as_field_group()`
method which renders the related elements of the field as a group, its _label_, _widget_, _errors_, and _help text_.

```html
<!-- app/templates/my_template.html -->
{{ form.non_field_errors }}
<form method="post" action="/myform/">
  {% csrf_token %}
  {{ form.name.as_field_group }}
  {{ form.email.as_field_group }}
  {{ form.message.as_field_group }}
  <button type="submit">Submit</button>
</form>
```

### Form Field Attributes

Each field has a number of attributes that can be used to customize the field. These attributes are:

- `label`: The label to use for the field.
- `help_text`: The help text to use for the field.
- `required`: A boolean that determines if the field is required.
- `disabled`: A boolean that determines if the field is disabled.
- `initial`: The initial value to use for the field.
- `errors`: List of errors associated with the field.
- `html_name`: The name of the field in the form.
- `form`: The form that the field belongs to.
- `field`: The field instance.
- `is_hidden`: A boolean that determines if the field is hidden.
- `template_name`: The name of the template to use for rendering the field.
- `value`: The value of the field.

`hidden_fields()` is a list of all hidden fields in the form. `visible_fields()` is a list of all visible fields in the
form.

## Model Form

A `ModelForm` is a form that is automatically created from a Django model. It is a subclass of `django.forms.ModelForm`.

```python
# app/forms.py
from django.forms import ModelForm

from .models import MyModel


class MyModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['field1', 'field2']
```

- ForeignKey is represented by django.forms.ModelChoiceField, which is a ChoiceField whose choices are a model QuerySet.
- ManyToManyField is represented by django.forms.ModelMultipleChoiceField, which is a MultipleChoiceField whose
  choices are a model QuerySet
- The form field’s label is set to the verbose_name of the model field, with the first character capitalized.
- The form field’s help_text is set to the help_text of the model field

### Saving a ModelForm

A `ModelForm` can be saved by calling the `save(commit=True)` method on the form instance. The `save()` method returns an instance
of the model that was saved. If the form is invalid, a `ValueError` will be raised.
If you call `save()` with `commit=False`, then it will return an object that hasn’t yet been saved to the database.

A side effect of using commit=False is seen when your model has a many-to-many relation with another model.
If your model has a many-to-many relation and you specify commit=False when you save a form, Django cannot immediately
save the form data for the many-to-many relation. This is because it isn’t possible to save many-to-many data for
an instance until the instance exists in the database. To work around this problem, every time you save a form using
commit=False, Django adds a save_m2m() method to your ModelForm subclass. After you’ve manually saved the instance
produced by the form, you can invoke save_m2m() to save the many-to-many form data.

### Selecting Fields to Use

The `fields` attribute of the `Meta` class can be used to specify the fields to use in the form. Set the fields
attribute to the special value `__all__` to indicate that all fields in the model should be used. set the `exclude`
attribute to specify the fields that should not be used in the form. If you set editable=False on the model field,
any form created from the model via ModelForm will not include that field.

Django will prevent any attempt to save an incomplete model, so if the model does not allow the missing fields
to be empty, and does not provide a default value for the missing fields, any attempt to save() a ModelForm
with missing fields will fail. To avoid this failure, you must instantiate your model with initial values for the
missing fields, either by providing a initial value for the field in the form definition or by setting the initial
parameter on the form instance.

```python
author = Author(title="Mr")
form = PartialAuthorForm(request.POST, instance=author)
form.save()
```

### Overriding and Customizing the Default Fields

To specify a custom widget for a field, use the widgets attribute of the inner Meta class. This should be a dictionary
mapping field names to widget classes or instances.

The widgets dictionary accepts either widget instances (e.g., Textarea(...)) or classes (e.g., Textarea).
Note that the widgets dictionary is ignored for a model field with a non-empty choices attribute. In this
case, you must override the form field to use a different widget.

Fields defined declaratively are left as-is, therefore any customizations made to Meta attributes such as
widgets, labels, help_texts, or error_messages are ignored; these only apply to fields that are generated
automatically.

Similarly, fields defined declaratively do not draw their attributes like max_length or required from the
corresponding model. If you want to maintain the behavior specified in the model, you must set the relevant
arguments explicitly when declaring the form field

```python
# app/forms.py
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from myapp.models import Author

class AuthorForm(ModelForm):
    slug = CharField(validators=[validate_slug])
    class Meta:
        model = Author
        
        fields = ["name", "title", "birth_date", "slug"]
        widgets = {"name": Textarea(attrs={"cols": 80, "rows": 20})}
        labels = {"name": _("Writer")}
        field_classes = {"slug": MySlugFormField}
        
        help_texts = {"name": _("Some useful help text.")}
        error_messages = {"name": {"max_length": _("This writer's name is too long.")}}

```

#### Customizing the Form Field

To customize the form field, you can subclass the form field and override the default behavior.

```python

### Validating Form Data on Multiple Fields

To validate form data on multiple fields, you can override the `clean()` method of the form class.

```python
# app/forms.py
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        if not name and not email and not message:
            raise forms.ValidationError('You must fill in at least one field.')
        return cleaned_data
```
