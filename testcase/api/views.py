from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination

from .serializers import (
    PostSerializer,
    FollowSerializer,
    BlogSerializer
)
from blogs.models import Post, Blog, Follow, ReadPost


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.request.user.posts

    def perform_create(self, serializer):
        serializer.save(blog=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        result = []
        posts = Post.objects.all(
            follower=get_object_or_404(Post, blog=self.request.user),
        ).all()
        for post in posts:
            result.append(
                ReadPost.objects.filter(
                    post=post,
                    blog=self.request.user,
                    is_read=False
                )
            )
        return QuerySet(result)

    def perform_create(self, serializer):
        serializer.save(
            blog=self.request.user
        )

    @action(
        methods=['GET'],
        detail=False
    )
    def mark_as_read(self, request):
        post = get_object_or_404(Post, id=request.get('post_id'))
        ReadPost.objects.get_or_create(
            post=post,
            blog=self.request.user,
            is_read=True
        )
