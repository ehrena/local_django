from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('hello/', TemplateView.as_view(template_name='main.html'), name='main'),
]

