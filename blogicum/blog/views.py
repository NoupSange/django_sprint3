from django.shortcuts import render, get_object_or_404

from blog.models import Category
from blog.utils import get_postlist


def index(request):
    post_list = get_postlist().select_related(
        'author', 'location', 'category')[0:5]
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        get_postlist(),
        pk=post_id
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(slug__exact=category_slug),
        is_published=True
    )

    post_list = get_postlist().select_related(
        'author', 'location', 'category'
    ).filter(category__slug__exact=category_slug)
    context = {
        'post_list': post_list,
        'category': category
    }
    return render(request, 'blog/category.html', context)
