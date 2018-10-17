from django.shortcuts import render

from dajngo.http import Http404

from blog.models import BlogPost

# Create your views here.

def index(request):
    blog_posts = BlogPost.objects.public()     #palauttaa kaikki blogipostukset joita ei ole astettu tulevaisuuteen

    return render(request, 'blog/index.html', {
        'blog_posts':blog_posts,
    })

def detail(request, post_id):
    try:
        blog_post = BlogPost.objects.public().get(pk=post_id)
    except BlogPost.DoeNotExist:
        raise Http404('Blogpost doesn exist')

    return render(request, 'blog/detail.html',{

    })