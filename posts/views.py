from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from posts.forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    ordering = ('-created_at',)
    paginate_by = 30


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:list')

    def form_valid(self, form):
        _object = form.save(commit=False)
        _object.user = self.request.user
        _object.profile = self.request.user.profile
        self.object = _object.save()
        return super(PostCreateView, self).form_valid(form)
