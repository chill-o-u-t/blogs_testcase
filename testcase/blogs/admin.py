from django.contrib import admin

from .models import Blog, Post, Follow, User, IsRead
# Register your models here.

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(User)
admin.site.register(IsRead)
