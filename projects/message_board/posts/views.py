from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
    template_name = 'posts/home.html'
    model = Post
