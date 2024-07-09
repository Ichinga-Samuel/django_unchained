from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    # success_url = '/articles/'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
