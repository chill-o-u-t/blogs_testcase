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

