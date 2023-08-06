from django.db import models


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


class Blog(models.Model):
    username = models.SlugField(

    )



