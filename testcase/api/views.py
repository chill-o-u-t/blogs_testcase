from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import (
    BlogSerializer,
    PostSerializer,
    FollowSerializer,
)
from .pagination import PagePagination

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
    pagination_class = PagePagination

    def get_blog(self):
        return get_object_or_404(Blog, author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(
            blog=self.get_blog()
        ).all()

    def perform_create(self, serializer):
        serializer.save(blog=self.get_blog())

    @action(
        methods=['GET'],
        detail=False
    )
    def mark_as_read(self):
        IsRead.objects.create(
            post=get_object_or_404(Post, blog=self.get_blog()),
            is_read=True
        )
        return self.queryset


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer

    def get_blog(self):
        return get_object_or_404(Blog, author=self.request.user)

    def get_queryset(self):
        posts = Follow.objects.filter(
            follower=self.request.user
        )
        is_not_read_posts = []
        for post in posts:
            read = IsRead.objects.filter(
                post=post,
                blog=self.get_blog()
            ).first()
            if read.is_read is True:
                break
            is_not_read_posts.append(post)
        return is_not_read_posts

    def perform_create(self, serializer):
        serializer.save(
            blog=self.get_blog(),
            post=get_object_or_404(Post, blog=self.get_blog())
        )
