from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import (
    BlogSerializer,
    PostSerializer,
    FollowSerializer,
    IsReadSerializer,
    UserSerializer
)

from blogs.models import (
    Post,
    Blog,
    User,
    Follow,
    IsRead
)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_blog(self):
        return get_object_or_404(Blog, author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(
            blog=self.get_blog()
        ).all()

    def perform_create(self, serializer):
        serializer.save(blog=self.get_blog())




