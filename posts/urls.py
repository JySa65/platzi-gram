from django.urls import path
from posts.views import PostListView, PostCreateView

app_name = "posts"

urlpatterns = [
    path('posts/', PostListView.as_view(), name="list"),
    path('posts/new', PostCreateView.as_view(), name="create")
]
