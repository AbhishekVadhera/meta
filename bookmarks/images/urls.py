from django.urls import path

from . import views


urlpatterns = [
    path('image_create/', views.image_create, name='image_create')
]
