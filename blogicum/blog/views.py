from django.http import Http404
from django.shortcuts import render, get_object_or_404

from blog.models import Category, Location, Post
from django.utils import timezone


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lt=timezone.now(), is_published=True, category__is_published=True
    ).select_related('author', 'location', 'category')[0:5]
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(is_published=True, pub_date__lt=timezone.now(), category__is_published=True),
        pk=pk
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    get_object_or_404(
        Category.objects.filter(slug__exact=category_slug),
        is_published=True
    )

    post_list = Post.objects.filter(
        category__slug__exact=category_slug,
        is_published=True,
        pub_date__lt=timezone.now()
    ).select_related('author', 'location', 'category')
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)
