from django.urls import path
from posts.views import PostListView, PostCreateView, PostDetailView

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name="list"),
    path('posts/new', PostCreateView.as_view(), name="create"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="detail")
]
