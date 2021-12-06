from django.urls import path

from .views import PostCreateView, PostListView, PostUpdateView

urlpatterns = [
    path("api/posts-list", PostListView.as_view(), name="posts-list"),
    path("api/create-post", PostCreateView.as_view(), name="create-post"),
    path("api/update-post/<int:pk>/", PostUpdateView.as_view(), name="update-post"),
]
