from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    BlogViewSet,
    PostViewSet
)

router_v1 = SimpleRouter()
router_v1.register(
    'blogs',
    BlogViewSet,
    basename='blog'
)
router_v1.register(
    r'blogs/(?P<blog_id>\d+)/posts',
    PostViewSet,
    basename='post'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
