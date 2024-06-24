from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='training-index'),
    path('about/', views.about, name='training-about'),
    path('courses/', views.courses, name='training-courses'),
    path('teachers/', views.teachers, name='training-teachers'),
]
