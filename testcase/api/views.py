from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (
    BlogSerializer,
    PostSerializer,
    IsReadSerializer,
    FollowSerializer
)
from .pagination import PagePagination

from blogs.models import (
    User,
    Post,
    IsRead,
    Follow
)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BlogSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = PagePagination

    def get_blog_id(self):
        return self.kwargs.get('blog_id')

    def get_queryset(self):
        return Post.objects.filter(
            blog__id=self.get_blog_id()
        )

    def perform_create(self, serializer):
        serializer.save(blog__id=self.get_blog_id())

    @action(
        methods=['GET'],
        detail=False
    )
    def mark_as_read(self, request, blog_id):
        obj = IsRead.objects.create(
            user=self.request.user,
            post__id=self.request.data['pk'],
            is_read=True
        )
        serializer = IsReadSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer

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
            follower=self.request.user
        )
