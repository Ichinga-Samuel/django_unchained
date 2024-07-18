from django.views.generic import ListView, DetailView, View, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Article
from .forms import CommentForm

class OwnObject(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user
    

class CommentGet(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    

class CommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view() 
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view() 
        return view(request, *args, **kwargs)
    
    
    
class ArticleDeleteView(LoginRequiredMixin, OwnObject, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    # success_url = '/articles/'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(LoginRequiredMixin, OwnObject, UpdateView):
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
    

