from django.urls import path
from . import views

urlpatterns = [
    path('add_comment/', views.add_comment, name='add_comment'),
    path('', views.comments_list, name='comments'),
    path('films/', views.film_list, name='film_list'),
]