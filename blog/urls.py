
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='bloghome'),
    path('<int:pk>/', views.blog_detail, name='blogdetail'),
]
