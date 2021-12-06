from django.urls import path

from .views import (
    PostCreateView,
    PostListView,
    PostUpdateDeleteView,
    CommentCreateView,
    PostDetailView,
    CommentUpdateDeleteView,
)

urlpatterns = [
    path("api/posts-list", PostListView.as_view(), name="posts-list"),
    path("api/post-detail/<int:pk>/", PostDetailView.as_view(), name="posts-detail"),
    path("api/create-post", PostCreateView.as_view(), name="create-post"),
    path(
        "api/update-delete-post/<int:pk>/",
        PostUpdateDeleteView.as_view(),
        name="update-delete-post",
    ),
    path(
        "api/create-comment/<int:post_pk>/",
        CommentCreateView.as_view(),
        name="create-comment",
    ),
    path(
        "api/update-delete-comment/<int:pk>/",
        CommentUpdateDeleteView.as_view(),
        name="update-delete-comment",
    ),
]
