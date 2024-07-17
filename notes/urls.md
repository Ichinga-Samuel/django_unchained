# Urls
Urls are used to map URLs to views. It is used to define the URL patterns for an app.

## Url Patterns
The urlpatterns list is a list of path instances. Each path() instance maps a URL pattern to a view.
```python
from django.urls import path
from .views import HomeView, ArticleView

urlpatterns = [
    path('home', HomeView.as_view(), name='name'),
    path('<int:id>/', ArticleView.as_view(), name='about'),
]
```
Path converters can be used to convert the URL string to the desired type. They have to be written a strict format
without spaces e.g. `<int:pk>`. The general format is `<type:value>` The path converters are:
- `str` - Matches any non-empty string, excluding the path separator, '/'
- `int` - Matches zero or any positive integer
- `slug` - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters
- `uuid` - Matches a UUID
- `path` - Matches any non-empty string, including the path separator, '/'
- `date` - Matches a string of the form YYYY-MM-DD
- `datetime` - Matches a string of the form YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
- `decimal` - Matches a decimal number
- `float` - Matches a floating-point number
- `list` - Matches a list of path converters
- `tuple` - Matches a tuple of path converters
