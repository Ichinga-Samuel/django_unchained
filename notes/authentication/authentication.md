# Authentication
Django helps in handling authentication via the `django.contrib.auth` module

### Templates
Account Handling templates should be ideally be in the **registration** folder in the toplevel templates folder.
Check if a user is authenticated in the template using `{% if user.is_authenticated %}`

### Views
Django provides views for handling authentication and user account action.

### LoginView
Handles login. Make sure `LOGIN_REDIRECT_URL = "home"` `LOGOUT_REDIRECT_URL = "home" ` is set in settings.py.

### Custom User Model
If changing the default user model, specify it in the settings `AUTH_USER_MODEL='accounts.CustomUser`.
The user model can be retrieved using `get_user_model()` from `django.contrib.auth`, or from the settings using `settings.AUTH_USER_MODEL`.

### Password Change
Django provides a view for password change. Add the *password_change_form.html* and *password_change_done.html* files
to the registration folder in the templates folder.

### Password Reset

Django provides a view for password reset. Add the following templates to the registration folder in the templates folder.
- *password_reset_form.html*
- *password_reset_done.html*
- *password_reset_confirm.html*
- *password_reset_complete.html*
Configure an email backend in settings.py to send emails.

```python
# email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

You can also have a custom email template for the password reset email. Create a `password_reset_email.html` file
in the registration folder in the templates folder. Add a text file for the email body and a text file for the email subject.
