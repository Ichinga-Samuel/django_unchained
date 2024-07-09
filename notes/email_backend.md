# Email
Setup and email backend for transactional emails. The default email backend is
`django.core.mail.backends.smtp.EmailBackend`. For development, use `django.core.mail.backends.console.EmailBackend` 
to print emails to the console.

## Mailjet
Mailjet is a transactional email service that can be used to send emails from the Django application.
Follow the steps below to set up Mailjet in Django.
- Create an account on [Mailjet](https://www.mailjet.com/)
- Activate the account
- Get started at the [Get Started](https://app.mailjet.com/auth/get_started/developer)
- Choose smtp relay
- Copy smtp server, usually `in-v3.mailjet.com`
- Port is `587` or `25`
- Retrieve the API key and secret key

Add the following to the `settings.py` file. Some of these values should be stored in environment variables.
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # you might need to comment this out
DEFAULT_FROM_EMAIL = 'my_email@gmail.com' # defaults to webmaster@localhost
EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_HOST_USER = 'api_key'
EMAIL_HOST_PASSWORD = 'api_secret'    
EMAIL_PORT = 587 # ssl port is 465
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False # only one of SSL or TLS can be true
```
## Custom Email Templates
To send custom email template create your own email template.
```python
