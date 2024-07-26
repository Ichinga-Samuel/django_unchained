<!-- TOC -->
- [Authentication in web requests](#authentication-in-web-requests)
  - [Login and Logout](#login-and-logout)
  - [Limiting User Access](#limiting-user-access)
    - [Login Restrictions](#login-restrictions)
      - [The login_required decorator](#the-login_required-decorator)
      - [Login Required Mixin](#login-required-mixin)
    - [Limiting access to logged-in users that pass a test](#limiting-access-to-logged-in-users-that-pass-a-test)
      - [User Passes Tests Decorator](#user-passes-tests-decorator)
      - [User Passes Test Mixin](#user-passes-test-mixin)
      - [The Permission Required Decorator](#the-permission-required-decorator)
      - [The PermissionRequiredMixin Mixin](#the-permissionrequiredmixin-mixin)
      - [Redirecting unauthorized requests in class-based views](#redirecting-unauthorized-requests-in-class-based-views)
    - [Authentication Views](#authentication-views)
      - [Common Methods and Attributes for All Authentication Views](#common-methods-and-attributes-for-all-authentication-views)
      - [LoginView](#loginview)
      - [Logout View](#logout-view)
      - [PasswordChangeView](#passwordchangeview)
      - [PasswordChangeDoneView](#passwordchangedoneview)
      - [PasswordResetView](#passwordresetview)
      - [PasswordResetDoneView](#passwordresetdoneview)
      - [PasswordResetConfirmView](#passwordresetconfirmview)
      - [PasswordResetCompleteView](#passwordresetcompleteview)
      - [PasswordResetConfirmView](#passwordresetconfirmview)
<!-- /TOC -->

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

### Authentication Views

Django provides several views that you can use for handling login, logout, and password management. These views make use
of the stock auth forms, but you can pass in your own forms as well. Authentication views expect there templates
at `templates/registration`.The urls mapping to these views are at `django.contrib.auth.urls`.
They can be introduced as shown below.

```python
# urls.py
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("accounts/", "django.contrib.auth.urls"),
    path()
]

# by importing the view directly you can change the url
urlpatterns = [
    path("signin/", LoginView.as_view())
]
```

#### Common Methods and Attributes for All Authentication Views

- `template_name`: By default all templates for authentication views are in the `template/registration` folder.
- `extra_context`: A dictionary of extra context for the template

#### LoginView

This view handles login. The url is at *login/*.

- `template_name`: the default is *registration/login.html.*
- `next_page`: defaults to *settings.LOGIN_REDIRECT_URL.*
- `redirect_field_name`: The GET field containing the URL to redirect to after login. Defaults to next.
- `authentication_form`: A callable (typically a form class) to use for authentication. Defaults to AuthenticationForm.
- `context variables`
  - `form`: A Form object representing the AuthenticationForm.
  - `next`: The URL to redirect to after successful login. This may contain a query string, too.
  - `site`: The current Site, according to the SITE_ID setting. If you don’t have the site framework installed, this will be set to an instance of  RequestSite, which derives the site name and domain from the current HttpRequest.
  - `site_name`: An alias for site.name

#### Logout View

Logs a user out on POST requests.

- URL name: *logout*, 
- template_name: *registration/logged_out.html.*
- next_page: The URL to redirect to after logout. Defaults to *settings.LOGOUT_REDIRECT_URL.*
- redirect_field_name: The GET field containing the URL to redirect to after logout. Defaults to *next*.
- Context Variables include `title` `site` and `site_name`.
- `logout_then_login(request, login_url=None)`: Logs a user out on POST requests, then redirects to the login page

#### PasswordChangeView

Allows a user to change their password.

- URL name: *password_change*
- template_name: *registration/password_change_form.html*
- success_url: The URL to redirect to after a successful password change. Defaults to *password_change_done*.
- form_class: The form class to use for changing the password. Defaults to *PasswordChangeForm*.
- Context Variables includes `form`

#### PasswordChangeDoneView

A view that is shown after a password change.

- URL name: *password_change_done*
- template_name: *registration/password_change_done.html*


#### PasswordResetView

Allows a user to reset their password using a one-time link. This can only be done for active users that have a valid
email address and usable password.

- URL name: *password_reset*
- template_name: *registration/password_reset_form.html*
- form_class: The form class to use for resetting the password. Defaults to *PasswordResetForm*.
- email_template_name: The template to use for the email sent to the user. Defaults to *registration/password_reset_email.html*.
- subject_template_name: The template to use for the email subject. Defaults to *registration/password_reset_subject.txt*.
- token_generator: The token generator to use for generating the one-time link. Defaults to *default_token_generator*.
- from_email: The email address to use for the email sent to the user. Defaults to *settings.DEFAULT_FROM_EMAIL*.
- success_url: The URL to redirect to after a successful password reset. Defaults to *password_reset_done*.
- html_email_template_name: The template to use for the HTML email sent to the user. Defaults to *None*.
- extra_email_context: A dictionary of extra context to use when rendering the email templates. Defaults to *None*.
- template_context: Template context includes the `form`.

Email template context include:

- `email`: The email address of the user.
- `user`: The current user.
- `domain`: The domain of the site from **site.domain** is site framework is installed, otherwise `request.get_host()`.
- `site_name`: An alias for **site.name**.
- `protocol`: **http** or **https** depending on the request.
- `uid`: The user’s primary key encoded in base 64.
- `token`: To check that the link is valid.

```html
Someone asked for password reset for email {{ email }}. Follow the link below:
{{ protocol}}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
```

#### PasswordResetDoneView

The view that is shown after a password reset email is sent.

- URL name: *password_reset_done*
- template_name: *registration/password_reset_done.html*

#### PasswordResetConfirmView

Present a form for a user to reset their password.

- `URL name`: *password_reset_confirm*
  - Keyword arguments: `uidb64` and `token`.
- `template_name`: *registration/password_reset_confirm.html*
- `token_generator`: Checks the password. Defaults to *default_token_generator*.
- `post_reset_login`: If True, logs the user in after a successful password reset. Defaults to *False*.
- `post_reset_login_backend`: The authentication backend to use for logging in after a successful password reset. Defaults to *None*.
- `form_class`: The form class to use for resetting the password. Defaults to *SetPasswordForm*.
- `success_url`: The URL to redirect to after a successful password reset. Defaults to *password_reset_complete*.
- `reset_url_token`: The token to use in the URL. Defaults to *token*.
- `template_context`: Template context includes the `form` and `validlink`.

#### PasswordResetCompleteView

The view that is shown after a password reset is complete.
