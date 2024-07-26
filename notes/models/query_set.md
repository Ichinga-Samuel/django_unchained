
#### get_or_create

Creates a new object with the given kwargs, if it doesn't already exist. Returns a tuple of (object, created),
where object is the retrieved or created object and created is a boolean specifying whether a new object was created.
Async version of `get_or_create` is `aget_or_create`.

```python
from myapp.models import MyModel

obj, done = MyModel.get_or_create(defaults=None, **kwargs)
```

#### update_or_create

Updates an object with the given kwargs, creating a new one if it doesn't already exist. Returns a tuple of (object, created),
where object is the retrieved or created object and created is a boolean specifying whether a new object was created.
Async version of `update_or_create` is `aupdate_or_create`.

```python
from myapp.models import MyModel

obj, done = MyModel.update_or_create(defaults=None, create_defaults={}, **kwargs)
```
