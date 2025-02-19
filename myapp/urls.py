from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload-success/', views.upload_success, name='upload_success'),
    path('images/', views.image_list, name='image_list'),
]
