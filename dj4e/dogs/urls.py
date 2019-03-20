from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.DogList.as_view(), name='dogs'),
    path('main/create/', views.DogCreate.as_view(), name='dog_create'),
    path('main/<int:pk>/update/', views.DogUpdate.as_view(), name='dog_update'),
    path('main/<int:pk>/delete/', views.DogDelete.as_view(), name='dog_delete'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]
