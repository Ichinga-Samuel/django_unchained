from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('pages.urls')),
    # namespace='pages' is used to avoid conflicts with other apps
    # pass a tuple of the app's urls and the app's name to include()
    # the namespace argument can then be used in the template to reference the app. it defaults to the app's name
    # if not provided
    path('', include(('pages.urls', 'pages'), namespace='pages'))
]
