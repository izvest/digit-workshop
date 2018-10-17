from djnago.urls import path
from blog.views from index

urlpatterns = [
    path('', index, name=(blog_index)),
    path('', include('blog.urls'))
]