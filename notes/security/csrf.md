# Cross Site Request Forgery (CSRF)

Cross Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application
in which they're authenticated. CSRF attacks specifically target state-changing requests, not theft of data,
since the attacker has no way to see the response to the forged request.

```python
# settings.py
CSFR_TRUSTED_ORIGINS = ['localhost:3000']
```
