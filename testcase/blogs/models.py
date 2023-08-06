from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField(
        max_length=254,
        unique=True,
        null=False,
        blank=False
    )
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )


class Blog(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False
    )
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='blogs'
    )

    def __str__(self):
        return f'{self.name}'


class Follow(models.Model):
    blog = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follows'
    )
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('blog', 'follower'), name='follow_unique'),
            models.CheckConstraint(
                check=~models.Q(blog=models.F('follower')),
                name='users_cannot_follow_themselves'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Post(models.Model):
    text = models.TextField(
        max_length=140
    )
    title = models.CharField(
        max_length=30,
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ('created_at',)


class IsRead(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='author'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='readed'
    )
    is_read = models.BooleanField(
        default=False
    )
