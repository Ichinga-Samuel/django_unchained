# Authentication Mixins

These mixins are used to require that a user be logged in or pass a test to access a view. They are used to restrict access to views
based on the user's authentication status or other criteria. The inherit from a base `AccessMixin` class.

### Login Required Mixin

The `LoginRequiredMixin` class is used to require that a user be logged in to access a view. It is a mixin class that can be
used with any view class.

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin):
    login_url = None # uses the LOGIN_URL setting by default
    permission_denied_message = ""
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME
```

### User Passes Test Mixin

The `UserPassesTestMixin` class is used to require that a user passes a test to access a view. It is a mixin class that can be
used with any view class. The `test_func` method should be overridden to return a boolean value.

```python
from django.contrib.auth.mixins import UserPassesTestMixin

class MyView(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
```
