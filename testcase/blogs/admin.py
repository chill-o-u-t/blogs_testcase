from django.contrib import admin

from .models import Post, Follow, User, IsRead

admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(User)
admin.site.register(IsRead)
