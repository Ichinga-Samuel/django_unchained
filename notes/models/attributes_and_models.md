# Models and Attributes

## Attributes

### objects

The most important attribute of a model is the Manager. It’s the interface through which database
query operations are provided to Django models and is used to retrieve the instancesfrom the database.
If no custom Manager is defined, the default name is *objects*. Managers are only accessible via model
classes, not the model instances.

## Methods

Define custom methods on a model to add custom“row-level”functionality to your objects. Whereas Manager
methods are intended to do“table-wide”things, model methods should act on a particular model instance.
This is a valuable technique for keeping business logic in one place –the model.

### Overriding predefined model methods

There’s another set of model methods that encapsulate a bunch of database behavior that you’ll want to
customize. In particular you’ll often want to change the way save() and delete() work.
You’re free to override these methods (and any other model method) to alter behavior.
A classic use-case for overriding the built-in methods is if you want something to happen whenever you save
an object.

## Model Inheritance

Model inheritance in Django works almost identically to the way normal class inheritance works in Python,
but the basics at the beginning of the page should still be followed. That means the base class should subclass `django.db.models.Model`.
There are three styles of inheritance that are possible in Django. Field name “hiding” is not permitted except when inherting from `Abstract Base Class`.

* Often, you will just want to use the parent class to hold information that you don’t want to have
    to type out for each child model. This class isn’t going to ever be used in isolation, so Abstract base classes are what you’re after.

* If you’re subclassing an existing model (perhaps something from another application entirely) and want each model to have its own database    table, Multi-table inheritance is the way to go.

## Abstract Base Class

Abstract base classes are useful when you want to put some common information into a number of other
models. You write your base class and put `abstract=True` in the Meta class. This model will then not be
used to create any database table. Instead, when it is used as a base class for other models, its fields will be
added to those of the child class. Fields inherited from abstract base classes can be overridden with another field or value, or be removed with None. If a child class does not declare its own Meta class, it will inherit the parent’s Meta, but abstract will be set to false.

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    class Meta:
        abstract = True

class Student(CommonInfo):
    # The Student model will have three fields: name, age and home_group
    home_group = models.CharField(max_length=5)
```

### Be careful with related_name and related_query_name

Use app_label and class name to customize *related_name* and *related_query_name* for subclasses of abstract class.

```python
from django.db import models
    class Base(models.Model):
        m2m = models.ManyToManyField(OtherModel,
         related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)ss",)
        class Meta:
            abstract = True
```

### Proxy Models

This is what proxy model inheritance is for: creating a proxy for the original model. You can create, delete
and update instances of the proxy model and all the data will be saved as if you were using the original (non proxied) model. The difference is that you can change things like the default model ordering or the default manager in the proxy, without having to alter the original.
Proxy models are declared like normal models. You tell Django that it’s a proxy model by setting the proxy
attribute of the Meta class to True.

```python
from django.db import models
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

 MyPerson(Person):
    class Meta:
        proxy = True
    def do_something(self):
    pass
```
