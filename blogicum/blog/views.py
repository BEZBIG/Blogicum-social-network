from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

POSTS_ON_PAGE = 5

def index(request):
    template = 'blog/index.html'
    published_posts = (
        Post.objects.select_related('category')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )
        .order_by('-pub_date')[:POSTS_ON_PAGE]
    )
    context = {'post_list': published_posts}
    return render(request, template, context)

def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    posts = (
        category.post_set.filter(
            is_published=True,
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')
    )
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)