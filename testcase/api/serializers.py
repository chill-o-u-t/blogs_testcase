from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..blogs.models import Blog, Follow, Post


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='author'
    )

    class Meta:
        model = Blog
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    blog = serializers.SlugRelatedField(
        read_only=True,
        slug_field='blog'
    )
    create_datetime = serializers.DateTimeField(
        read_only=True
    )
    is_rear = serializers.SerializerMethodField(

    )

    class Meta:
        model = Post
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    followed = serializers.SlugRelatedField(
        read_only=True,
        slug_field='followed',
        default=serializers.CurrentUserDefault()
    )
    follower = serializers.SlugRelatedField(
        required=True,
        slug_field='follower',
        queryset=Blog.objects.all()
    )

    def validate_following(self, following):
        author = self.context['request'].blog
        if author != following:
            return following
        raise serializers.ValidationError('Нельзя подписаться на самого себя')

    class Meta:
        fields = ('followed', 'follower')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['followed', 'follower']
            )
        ]


class ReadBlogSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
    )
    blog = serializers.SlugRelatedField(
        read_only=True
    )
