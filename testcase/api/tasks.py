from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celery_app import app
from blogs.models import Post, Follow, User


RENDER_REMPLATE = """ 
Five last posts from your follows

{% for post in posts %} 
"{{ post.title }}"
{{ post.text }}
<------------------->
{% endfor %} 
"""


@app.task
def send_last_posts():
    for user in User.objects.all():
        posts = Post.objects.filter(
            blog__follower__user=user
        ).order_by('created_at')[:5]
        if not posts:
            continue

        template = Template(RENDER_REMPLATE)

        send_mail(
            'Your follows blogs',
            template.render(context=Context({'posts': posts})),
            'fromtestcase@test.ru',
            [user.email],
            fail_silently=False
        )
