## Viewsets

A viewset is a way to combine the logic for multiple related views into a single class. In other
words, one viewset can replace multiple views.

```python
# views.py
from rest_framework import viewsets

from .models import MyModel
from .serializers import MyModelSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

## Routers

Routers work directly with viewsets to automatically generate URL patterns for us. Our
current posts/urls.py file has four URL patterns: two for blog posts and two for users. We can
instead adopt a single route for each viewset

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import MyModelViewSet

router = SimpleRouter()
router.register('mymodel', MyModelViewSet, basename='mymodel')

urlpatterns = router.urls
``` 
