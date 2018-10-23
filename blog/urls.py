from django.urls import path

from blog.views import BlogPostViewSet, index, post_detail

urlpatterns = [
    path('', index, name='blog-index'),
    path('post/<int:post_id>/', post_detail, name='blog-detail'),
    path('api/blog-posts/', BlogPostViewSet.as_view({'get': 'list'}), name='api-blog-posts'),
]
