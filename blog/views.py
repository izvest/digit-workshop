from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


def index(request):
    blog_posts = BlogPost.objects.public()

    return render(request, 'blog/index.html', {
        'blog_posts': blog_posts,
    })


def post_detail(request, post_id):
    try:
        blog_post = BlogPost.objects.public().get(pk=post_id)
    except BlogPost.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'blog/detail.html', {
        'blog_post': blog_post,
    })


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.public()
    serializer_class = BlogPostSerializer
