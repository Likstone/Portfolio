from django.urls import path
from . import views

urlpatterns = [
    path('', views.Standart),
    path('about', views.About),
    path('contact', views.Contact),
]
