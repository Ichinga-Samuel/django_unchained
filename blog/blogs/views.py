from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Blog


class BlogsHomeViews(ListView):
    # Default context_object_name is <model_name_list> in lowercase
    model = Blog
    template_name = 'home.html'


class BlogDetailView(DetailView):
    # Default context_object_name is model name in lowercase or object
    model = Blog
    # blog_detail.html is in the blogs app directory
    template_name = 'blogs/blog_detail.html'


class BlogCreateView(CreateView):
    model = Blog
    # use '__all__' to include all fields in the form
    fields = ['title', 'author', 'body', ]
    template_name = 'blogs/new_blog.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body']
    template_name = 'blogs/blog_update.html'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('home')
    # success_url = '/' # this is also valid but reverse_lazy is preferred as this is hard-coded
