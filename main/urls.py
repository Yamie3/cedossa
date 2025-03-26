from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
        path('about/', views.about, name='about'),  # About page
]
