from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination

from .serializers import (
    PostSerializer,
    FollowSerializer,
    BlogSerrializer
)
from blogs.models import Post, Blog, Follow


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerrializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs.get('blog_id')).posts

    def perform_create(self, serializer):
        serializer.save(blog__user=self.request.user)

    @action(
        methods=['GET'],
        detail=False
    )
    def mark_as_read(self, request):
        post = get_object_or_404(Post, id=request.get('post_id'))
        post.is_read = True


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    pagination_class = LimitOffsetPagination

    def get_blog(self):
        return get_object_or_404(Blog, id=self.request.get('blog_id'))

    def get_queryset(self):
        return Post.objects.all(
            folower__blog=self.get_blog()
        ).all()

    def perform_create(self, serializer):
        serializer.save(
            blog=self.get_blog()
        )

