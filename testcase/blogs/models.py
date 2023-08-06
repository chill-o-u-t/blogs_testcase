from django.db import models


class Blog(models.Model):
    username = models.SlugField(
        unique=True,
        max_length=20,
    )


class Post(models.Model):
    test = models.TextField(max_length=140)
    title = models.CharField(
        max_length=20,
        null=False
    )
    create_datetime = models.DateTimeField(
        auto_now_add=True
    )
    is_read = models.BooleanField(
        default=False
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='posts'
    )


class Follow(models.Model):
    followed = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='author',
    )
    follower = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='follower'
    )



