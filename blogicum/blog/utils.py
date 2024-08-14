from blog.models import Post
from django.utils import timezone


def get_postlist():
    post_list = Post.objects.filter(
        pub_date__lt=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return post_list
