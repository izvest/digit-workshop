from django.urls import path
from foli.views import home, stop_detail

urlpatterns = [
    path('', home, name='home'),
    path('<int:stop_id>/', stop_detail, name='stop-detail'),
    path('<str:stop_id>/', stop_detail, name='stop-detail'),
]