from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views
urlpatterns = [
    path('', views.index),
    path('error',TemplateView.as_view(template_name='failed.html')
         , name='error'),
]
