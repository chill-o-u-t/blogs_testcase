from rest_framework import serializers

from blogs.models import User, Post, IsRead, Follow
from rest_framework.validators import UniqueTogetherValidator


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'blog'
        )


class PostSerializer(serializers.ModelSerializer):
    blog = serializers.SlugRelatedField(
        read_only=True,
        slug_field='blog'
    )

    class Meta:
        model = Post
        fields = '__all__'


class IsReadSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=serializers.CurrentUserDefault
    )
    blog = serializers.SlugRelatedField(
        slug_field='blog',
        queryset=serializers.CurrentUserDefault
    )

    class Meta:
        model = IsRead
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='follower',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='blog',
        queryset=User.objects.all(),
        required=True
    )

    def validate_following(self, following):
        user = self.context['request'].user
        if user != following:
            return following
        raise serializers.ValidationError('Нельзя подписаться на себя')

    class Meta:
        model = Follow
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['blog', 'following']
            )
        ]
