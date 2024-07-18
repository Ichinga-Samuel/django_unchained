# Authentication in web requests

Django uses sessions and middleware to hook the authentication system into request objects.
These provide a request.user attribute on every request which represents the current user. If the current
user has not logged in, this attribute will be set to an instance of AnonymousUser, otherwise it will be an
instance of User.

## Login and Logout

Use the `login, authenticate and logout` funcions to handle user sessions

```python
from django.contrib.auth import login, authentication, logout

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password) # returns user if successfull or none
    if user is not None:
        login(request, user)


def logout(request):
    logout(request)  # clears the session
```

## Limiting User Access

The raw way to limit access to pages is to check `request.user.is_authenticated` and either redirect to a login page.  But this can be better done with decorators and mixins

### Login Restrictions

#### The login_required decorator

```python
from django.contrib.auth.decorators import login_required

# optional login_url, if not provided, make sure settings.LOGIN_URL has been set.
@login_required(redirect_field_name='next', login_url=None) 
def login_view(request):
    ...
```

#### Login Required Mixin

The `LoginRequiredMixin` class is used to require that a user be logged in to access a view. It is a mixin class that can be used with any view class.

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin):
    login_url = None # uses the LOGIN_URL setting by default
    permission_denied_message = ""
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME
```

### Limiting access to logged-in users that pass a test

This limits access based on certain permissions or some other test

#### User Passes Tests Decorator

As a shortcut, you can use the convenient `user_passes_test` decorator which performs a redirect when
the callable returns False.

```python
from django.contrib.auth.decorators import user_passes_test

def test_func(user):
    return user.email.endswith("@example.com")

@user_passes_test(email_check)
    def my_view(request):
        ...
```

#### User Passes Test Mixin

The `UserPassesTestMixin` class is used to require that a user passes a test to access a view. It is a mixin class that can be
used with any view class. The `test_func` method should be overridden to return a boolean value.

```python
from django.contrib.auth.mixins import UserPassesTestMixin

class MyView(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
```

#### The Permission Required Decorator

It’s a relatively common task to check whether a user has a particular permission. For that reason,
Django provides a shortcut for that case: the permission_required() decorator.

```python
from django.contrib.auth.decorators import permission_required

@permission_required("polls.addchoice", login_url=None, raise_exception=False)  # <app_name>.<permission>
def my_view(request):
    ...
```

#### The PermissionRequiredMixin Mixin

To apply permission checks to class-based views, you can use the PermissionRequiredMixin

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = "polls.add_choice"
    # Or multiple of permissions:
    permission_required = ["polls.view_choice", "polls.change_choice"]

    # You may also override these methods:
    def get_permission_required():
        # Returns an iterable of permission names used by the mixin. Defaults to the permission_required     attribute, converted to a tuple if necessary.
    
    def has_permission():
        # Returns a boolean denoting whether the current user has permission to execute the decorated view.
```

#### Redirecting unauthorized requests in class-based views

To ease the handling of access restrictions in class-based views, the `AccessMixin` can be used to configure
the behavior of a view when access is denied.

```python
class AccessMixin:
    """
    Abstract CBV mixin that gives access mixins the same customizable
    functionality.
    """
    login_url = None
    permission_denied_message = ""
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_login_url(self):
        """
        Override this method to override the login_url attribute.
        """

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """

    def get_redirect_field_name(self):
        """
        Override this method to override the redirect_field_name attribute.
        """

    def handle_no_permission(self):
        """Depending on the value of raise_exception, the method either raises a PermissionDenied exception or redirects the user to the login_url,"""
```

### Authentication View

Django provides several views that you can use for handling login, logout, and password management. These
make use of the stock auth forms but you can pass in your own forms as well. Authentication views expect there templates at `templates/registration`. Urls mapping to this views are at `django.contrib.auth.urls`

