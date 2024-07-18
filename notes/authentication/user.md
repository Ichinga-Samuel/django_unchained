# User Objects

User objects are the core of the authentication system. They typically represent the people interacting with
your site and are used to enable things like restricting access, registering user profiles, associating content
with creators etc. Only one class of user exists in Django’s authentication framework, i.e., 'superusers' or
admin 'staff' users are just user objects with special attributes set, not different classes of user objects.
The primary attributes of the default user are: `username, password, email, first_name, last_name`. It also has two 
many_to_many fields, `groups and user_permissions`.

## Creating User

The most direct way to create users is to use the included `create_user()` helper function.

```python
from django.contrib.auth.models import User
user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
user.last_name = 'Ono'
user.save()
```

### Creating Superuser

Create superusers using the createsuperuser command:

```bash
python manage.py createsuperuser --username=joe --email=joe@example.com # can also be called without arguments
```

### Change Password

Password can be changed either from the command line, the admin panel or programatically

```bash
python manage.py changepassword <username>
```

```python
from django.contrib.auth.models import User

user = User.objects.get(name='john')
user.set_password('passwword12*')
u.save()
```

### Authenticating Users

Use authenticate() to verify a set of credentials. It takes credentials as keyword arguments, username
and password for the default case, checks them against each authentication backend.

```python
from django.contrib.auth import authenticate

# this a low leve code for authentication
user = authenticate(username='useradmin', password='password1')  # returns user object or None
```

## Permissions and Authorization

Django comes with a built-in permissions system. It provides a way to assign permissions to specific users
and groups of users. Permissions can be set not only per type of object, but also per specific object instance.
By using the `has_view_permission()`, `has_add_permission()`, `has_change_permission()` and `has_delete_permission()` methods provided by the `ModelAdmin` class
User objects have two many-to-many fields: `groups` and `user_permissions`.

### Default Permissions

Assuming you have an application with an `app_label foo` and a model named `Bar`, to test for basic permissions you should use:

* add: user.has_perm('foo.add_bar')
* change: user.has_perm('foo.change_bar')
* delete: user.has_perm('foo.delete_bar')
* view: user.has_perm('foo.view_bar')

The format then is `<app_label>.<permission>.<model>`. Model name must be in lowercase.

### Groups

`django.contrib.auth.models.Group` models are a generic way of categorizing users so you can apply permissions, or some other label, to those users. A user can belong to any number of groups.

### Programmatically creating permissions

While custom permissions can be defined within a model’s Meta class, you can also create permissions directly. For example, you can create the can_publish permission for a BlogPost model in myapp.

```python
from myapp.models import BlogPost, BlogPostProxy
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(BlogPost)
permission = Permission.objects.create(codename="can_publish", name="Can Publish Posts", content_type=content_type)

# for proxy model set for_concrete_model=False
content_type = ContentType.objects.get_for_model(BlogPostProxy, for_concrete_model=False)
```

add permission to a user

```python
from myapp.models import MyModel
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission
from djang.contrib.contenttypes.models import ContentType

user = get_object_or_404(User, pk=user_id)
res = user.has_perm('can_change')
if not res:
    content_type = ContentType.get_for_model(MyModel)
    cc = Permission.objects.get(codename='can_change', content_type=content_type)
    user.user_permissions.add(cc)

    # due to modelbackend caching, you need to refetch the user object to confirm the permission has been added.
```
