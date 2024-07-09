from django.urls import path
from .views import home_page as home_view, HomePageView, AboutPageView

urlpatterns = [
    path('func/', home_view),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
