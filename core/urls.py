from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import QueueListView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('queue', QueueListView.as_view(), name='queue-list'),
    path('error',TemplateView.as_view(template_name='failed.html')
         , name='error'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)