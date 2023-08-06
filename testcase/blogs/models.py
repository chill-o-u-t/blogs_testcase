from django.contrib.auth import get_user_model
from django.db import models


class Blog(models.Model):
    author =models.CharField(
        null=False,
        max_length=16
    )

    def __str__(self):
        return f'{self.author}'


class Post(models.Model):
    text = models.TextField(max_length=140)
    title = models.CharField(
        max_length=20,
        null=False
    )
    create_datetime = models.DateTimeField(
        auto_now_add=True,
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return f'{self.text[:30]}'

    class Meta:
        ordering = ('create_datetime',)


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



