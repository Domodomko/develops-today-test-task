from celery import shared_task
from .models import Post


@shared_task
def reset_post_upvotes():
    posts = list(Post.objects.exclude(upvotes_ammount=0))
    for post in posts:
        post.upvotes_ammount = 0

    Post.objects.bulk_update(posts, ["upvotes_ammount"])
