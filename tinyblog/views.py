from django.views import generic
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleForm


class IndexView(generic.ListView):
    model = Article


class DetailView(generic.DetailView):
    model = Article


class CreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('tinyblog:index')


class EditView(generic.UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('tinyblog:index')

class DeleteView(generic.DeleteView):
    model = Article
    success_url = reverse_lazy('tinyblog:index')
