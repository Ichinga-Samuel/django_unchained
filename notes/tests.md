# Testing

Django has a test framework that can be used to test the apps. The tests are written in the tests.py file of the app.
For simple non database tests, the SimpleTestCase class can be used.

```bash
# Run tests for all apps
python manage.py test

# Run tests for a specific app
python manage.py test <app_name.tests>
```
