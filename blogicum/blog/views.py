from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    context = {'post': posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    context = {'category': category_slug}
    return render(request, 'blog/category.html', context)