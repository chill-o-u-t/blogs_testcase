from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from blogs.models import User, Blog, Post, Follow, IsRead


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )


class PostSerializer(serializers.ModelSerializer):
    blog = serializers.SlugRelatedField(
        read_only=True,
        slug_field='blog'
    )

    class Meta:
        model = Post
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='author',
        read_only=True
    )

    class Meta:
        model = Blog
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    pass


class IsReadSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='user'
    )
    blog = serializers.SlugRelatedField(
        required=True,
        slug_field='blog'
    )

    class Meta:
        model = IsRead
        fields = '__all__'
