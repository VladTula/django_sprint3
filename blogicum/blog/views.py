from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.utils import timezone


def get_filter():
    return Post.objects.filter(pub_date__lt=timezone.now(),
                               is_published=True, category__is_published=True
                               ).select_related('category')

def index(request):
    context = {'post_list': get_filter()[0:5]}
    return render(request, 'blog/index.html', context)

def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.filter(is_published=True),
                                 slug=category_slug)
    post_list = get_filter().filter(category__title=category.title)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(get_filter(), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)