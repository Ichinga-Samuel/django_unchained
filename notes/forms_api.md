# The Form Class

Form class describes a form and determines how it works and appears. It can either be _bound_ or _unbound_.
To bind data to a form, pass the data as a dictionary as the first parameter to your Form class constructor.
The keys are the field names, which correspond to the attributes in your Form class.
The values are the data you’re trying to validate.

```python

data = {"subject": "hello", "message": "Hi there", "sender": "foo@example.com", "cc_myself": True}
f = ContactForm(data)
f.is_bound  # True
```

## Form Errors

If the form is bound and the data is invalid, the form will contain errors. The form’s data will be validated the first
time either you call `is_valid()` or access `errors`.
Access the errors attribute to get a dictionary of error messages. `form.errors` is a dictionary of lists of errors.
In this dictionary, the keys are the field names, and the values are lists of strings representing the error
messages. The error messages are stored in lists because a field can have multiple error messages.

### Form.errors.as_data and Form.errors.as_json

Returns a dict that maps fields to their original ValidationError instances.
`Form.errors.as_json(escape_html=False)` Returns the errors serialized as JSON.

### Form.errors.add_error

The `Form.add_error(field, error)` Adds a new error to the form. This method is used by the form’s `clean()` method
to attach any errors that aren’t specific to a particular field. The field argument is the name of the field to which
the errors should be added.If its value is None the error will be treated as a non-field error as returned by
`Form.non_field_errors()`. The error argument can be a simple string or an instance of `ValidationError`.

### Form.has_error

The `Form.has_error(field, code=None)` method returns a boolean designating whether a field has an error with a specific
error code. If code is None,
it will return True if the field contains any errors at all. To check for non-field errors use `NON_FIELD_ERRORS`
as the field parameter.

### Form.non_field_errors

The `Form.non_field_errors()` method returns the list of errors from Form.errors that aren’ t associated with a
particular field. This
includes ValidationErrors that are raised in Form.clean() and errors added using Form.add_error(None, "...")

### Adding initial Data to Unbound Form

An unbound form is a form that has not been submitted. It is created by instantiating the form class without any data.
Use initial to declare the initial value of form fields at runtime. For example, you might want to fill in a
username field with the username of the current session. The initial argument is a dictionary that maps field names
to initial values. `f = ContactForm(initial={"subject": "Hi there!"})`

### Checking which form data has changed

The `Form.has_changed()` method returns True if data in the form differs from the initial data.
`Form.changed_data` attribute returns a list of the names of the fields whose values in the form’ s bound data

```python
f = ContactForm(request.POST, initial=data)
f.has_changed()  # True
f.changed_data  # ['subject', 'message']
```

## Form Fields

A form field is a single piece of data. It is a class that validates input and converts it to a Python-compatible type.

```python
f = ContactForm()
for row in f.fields.values():
    print(row)
```

### Accessing Clean Data

The `Form.cleaned_data` attribute is a dictionary of validated and normalized form data. It is only available on bound

## Default Rendering

Django provides a default way to render forms. The `{{ form }}` template tag displays the form.

### template_name

The `template_name` attribute is used to specify the template to use for rendering the form.

### render

The `Form.render(template_name=None, context=None, renderer=None)` method renders the form as HTML.

### get_context

The `Form.get_context()` method returns the context data for rendering the form.
The available context is:

- `form`: The bound form.
- `fields`: All bound fields, except the hidden fields.
- `hidden_fields`: All hidden bound fields.
- `errors`: All non field related or hidden field related form errors.
