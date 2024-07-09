# Models

A model is the single, definitive source of information about your data. It contains the essential fields and
behaviors of the data you’ re storing. Generally, each model maps to a single database table.
The basics:
1. [ ] Each model is a Python class that subclasses django.db.models.Model.
2. [ ] Each attribute of the model represents a database field.
3. [ ] With all of this, Django gives you an automatically-generated database-access API;

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

## Fields
The most important part of a model – and the only required part of a model – is the list of database fields it defines.
Fields are specified by class attributes. Be careful not to choose field names that conflict with the models 
API like clean, save, or delete.

### Field types
Each field in your model should be an instance of the appropriate Field class. Django uses the field class
types to determine a few things:
* The column type, which tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT).
* The default HTML widget to use when rendering a form field (e.`g. <input type="text">, <select>`).
* The minimal validation requirements, used in Django’ s admin and in automatically-generated forms.

### Field options
Each field takes a certain set of field-specific arguments (e.g. max_length for CharField, default for
DateTimeField). The following are common arguments for all field types:
* `null`: If True, Django will store empty values as NULL in the database. Default is False.
* `blank`: If True, the field is allowed to be blank. Default is False. This means that in forms, the field will not be required.
* `choices`: A group of choices for this field. If this is provided, 
             the default form widget will be a select box with these choices instead of the standard text field.
             it can be a list of tuples, a mapping or any callable that returns such suitable data type.
```python
# The first element in each tuple is the value that will be stored in the database. 
# The second element is displayed by the field’ s form widget
gender = [
    ('M', 'Male'),
    ('F', 'Female')
]
```

* `default`: The default value for the field. This can be a value or a callable object.
              If callable it will be called every time a new object is created.

* `help_text`: Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.
* `primary_key`: If True, this field is the primary key for the model.
* `unique`: If True, this field must be unique throughout the table.

>The primary key field is read-only. If you change the value of the primary key on an existing object
and then save it, a new object will be created alongside the old one.

## Relationships
Django offers ways to define the three most common types of database relationships: many-to-one, many-to-many and one-to-one.

### Many-to-one relationships
To define a many-to-one relationship, use `django.db.models.ForeignKey`.You use it just like any other 
Field type: by including it as a class attribute of your model, but it requires a positional argument i.e. the class
to which the model is related.
```python
# For example, if a Car model has a Maker –that is, a Maker makes multiple cars but each Car
# only has one Maker– you’d define the Car model like this:

from django.db import models

class Maker(models.Model):
    name = models.CharField(max_length=30)

class Car(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
```
You can also create recursive relationships (an object with a many-to-one relationship to itself) and relationships to 
models not yet defined; see the model field reference for details.
It’ s suggested, but not required, that the name of a ForeignKey field (manufacturer in the example above)
be the name of the model, lowercase. You can call the field whatever you want.

### Many-to-many relationships
To define a many-to-many relationship, use `django.db.models.ManyToManyField`. 
For example, if a Pizza has multiple Topping objects –that is, a Topping can be on multiple pizzas and each
Pizza has multiple toppings
```python
from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)
```

You can also create recursive relationships (an object with a many-to-many relationship to itself) and relationships to
models not yet defined. It doesn’ t matter which model has the ManyToManyField, but you should only put it in one of the models –
not both.

#### Extra fields on many-to-many relationships

An intermediate model can be created for holding information about the relationship.
This model is associated with the ManyToManyField using the `through` argument.
An example is shown in [example](../../django_tutorial/band/models.py). Calling **clear()** on a many-to-many relationship manger
can be used to remove all the relationships and delete the intermediate model instances.

### One-to-one relationships

To define a one-to-one relationship, use `OneToOneField`. This works exactly like `ForeignKey`,
but it creates a one-to-one relationship. A one-to-one relationship is basically a way of extending a model with
another model using inheritance.

### Field Name Restrictions

* A field name cannot be a Python reserved word, because that would result in a Python syntax error.

* A field name cannot contain more than one underscore in a row, due to the way Django’s query lookup
  syntax works it can not also end with an underscore.

> These limitations can be worked around, though, because your field name doesn’t necessarily have to match your database column name. See the db_column option.

### Meta Options

Give your model metadata by using an inner class Meta

```python
class Ox(models.Model):
    horn_length = models.IntegerField()
    
    class Meta:
        ordering = ["horn_length"]  # specify odering 
        verbose_name_plural = "oxen" # 
```
