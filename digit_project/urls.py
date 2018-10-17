from django.conf import settings
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('da/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('blog.urls'))
]

if settings.DEBUG:
    # Serve media from development server
    from django.conf.urls.static import static
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
