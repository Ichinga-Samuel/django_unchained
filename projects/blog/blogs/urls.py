from django.urls import path

from .views import BlogsHomeViews, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogsHomeViews.as_view(), name='home'),
    # specify the primary key of the blog object in the URL
    # parameters are passed to the views as arguments
    # the type must be specified in the format <type:param>
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', BlogCreateView.as_view(), name='new_blog'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
