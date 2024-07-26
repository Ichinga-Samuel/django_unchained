<!-- TOC -->

- [User Object](#user-object)
  - [Creating User](#creating-user)
    - [Creating Superuser](#creating-superuser)
    - [Change Password](#change-password)
  - [Authenticating Users](#authenticating-users)
    - [Permissions and Authorization](#permissions-and-authorization)
    - [Default Permissions](#default-permissions)
    - [Groups](#groups)
    - [Programmatically creating permissions](#programmatically-creating-permissions)
  - [Extending Custom User Model](#extending-custom-user-model)
    - [AbstractUser and AbstractBaseUser](#abstractuser-and-abstractbaseuser)
    - [Writing a Custom Manager](#writing-a-custom-manager)
    - [Custom User and Admin](#custom-user-and-admin)

<!-- /TOC -->

# User Object

The User object is at the core of the authentication system. They typically represent the people interacting with
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

## Authenticating Users

Use authenticate() to verify a set of credentials. It takes credentials as keyword arguments, username
and password for the default case, checks them against each authentication backend.

```python
from django.contrib.auth import authenticate

# this a low leve code for authentication
user = authenticate(username='useradmin', password='password1')  # returns user object or None
```

### Permissions and Authorization

Django comes with a built-in permissions system. It provides a way to assign permissions to specific users
and groups of users. Permissions can be set not only per type of object, but also per specific object instance.
By using the `has_view_permission()`, `has_add_permission()`, `has_change_permission()` and `has_delete_permission()`
methods provided by the `ModelAdmin` class User objects have two many-to-many fields: `groups` and `user_permissions`.

### Default Permissions

Assuming you have an application with an `app_label foo` and a model named `Bar`, to test for basic permissions you should use:

* add: user.has_perm('foo.add_bar')
* change: user.has_perm('foo.change_bar')
* delete: user.has_perm('foo.delete_bar')
* view: user.has_perm('foo.view_bar')

The format then is `<app_label>.<permission>.<model>`. Model name must be in lowercase.

### Groups

`django.contrib.auth.models.Group` models are a generic way of categorizing users so you can apply permissions, or some
other label, to those users. A user can belong to any number of groups.

### Programmatically creating permissions

While custom permissions can be defined within a model’s Meta class, you can also create permissions directly.
For example, you can create the can_publish permission for a BlogPost model in myapp.

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

## Extending Custom User Model

The user model can be extended by creating a custom user model that subclasses `AbstractUser` or `AbstractBaseUser` or
by using a proxy model. The former is more flexible and allows for more customization.

### AbstractUser and AbstractBaseUser

Django allows you to override the default user model by providing a value for the AUTH_USER_MODEL setting
that references a custom model. This model can be accessed by calling `get_user_model()` from `django.contrib.auth`.
Use `AbstractUser` if you want to keep the default fields and add more fields. Use `AbstractBaseUser` if you want to
start from scratch.

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
```

The easiest way to construct a compliant custom user model is to inherit from AbstractBaseUser.It provides the core
implementation of a user model, including hashed passwords and tokenized password resets. You must then provide some
key implementation details: 

- `USERNAME_FIELD`: The field that is used for authentication. This is usually a unique field such as email or username.
- `EMAIL_FIELD`: The field that is used for email. This is usually a unique field such as email or username.
- `REQUIRED_FIELDS`: A list of fields that are required when creating a user via the createsuperuser management command.
- `is_active`: A boolean that determines whether the user is active.
- `get_full_name()`: A method that returns the user’s full name. This is used in the Django admin and is **optional**.
- `get_short_name()`: A method that returns the user’s short name. This is used in the Django admin and is **optional**.

Methods and attributes includes.

- `is_authenticated`: Read only attribute that is always True for a user instance.
- `is_anonymous`: Read only attribute that is always False for a user instance.
- `get_username()`: Returns the username for the user as specified by the USERNAME_FIELD.
- `clean()`: Normalizes the username using the normalize_username() method.
- `normalize_username()`: Normalizes the username using the model’s USERNAME_FIELD.
- `set_password(raw_password)`: Sets the user’s password to the given raw password taking care of the password hashing.
- `check_password(raw_password)`: Returns True if the given raw password is the correct password for the user.
- `set_unusable_password()`: Marks the user as having no password set.
- `has_usable_password()`: Returns True if the user has a password set.
- `get_session_auth_hash()`: Returns an HMAC of the password field.
- `get_email_field_name()`: Returns the name of the email field.

```python

The example below makes use of the AbstractBaseUser class to create a custom user model.

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

```

### Writing a Custom Manager

A custom manager is required to manage the custom user model. It should subclass `BaseUserManager` and override the
`create_user()` and `create_superuser()` methods.

- `create_user(username_field, password=None, **required_fields)`: Creates and returns a user with an email, password and the required fields.
- `create_superuser(username_field, password=None, **required_fields)`: Creates and returns a superuser with an email, password and the required fields.

```python
class UserManager(BaseUserManager):
    def create_user(self, *, username: str, email: str = '', password: str = '', **kwargs):
        user = self.model(email=self.normalize_email(email), username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, *, email: str, username: str, password: str = ''):
        self.create_user(email=email, username=username, password=password, verified=True, is_admin=True)
```

### Custom User and Admin

To be able to use the custom user model in the admin panel, you need to create a custom user admin class that
has the following attributes:

- `is_active`: A boolean that determines whether the user is active.
- `is_staff`: A boolean that determines whether the user is a member of the staff.
- `has_module_perms(app_label)`: Returns True if the user has permissions to view the app with the given app_label.
- `has_perm(perm, obj=None)`: Returns True if the user has the specified permission.

Also, you might need to add the permissions mixins to the custom user model.
