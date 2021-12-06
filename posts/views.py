from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer, CommentSerializer, PostWithCommentsSerializer
from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly


class PostCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permissions = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).prefetch_related("author")

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permissions = [IsAuthenticated, IsOwnerOrReadOnly]


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().prefetch_related("author")


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostWithCommentsSerializer
    queryset = Post.objects.all().prefetch_related("author", "comments__author")


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permissions = [IsAuthenticated]

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(
                author=self.request.user,
                post=Post.objects.get(pk=self.kwargs.get("post_pk")),
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permissions = [IsAuthenticated, IsOwnerOrReadOnly]
