from django.urls import path
from djangomidapp import views

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('products/', views.products, name='product'),
   path('remote/', views.remote, name='remote'),
   path('videos/', views.videos, name='video')

]
