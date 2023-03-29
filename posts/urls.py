from django.urls import path
from . import views

urlpatterns = [
  path('allposts/', views.getPosts),
  path('add/', views.addPost),
  path('edit/<int:id>/', views.editPost),
  path('view/<int:id>/', views.viewPost),
  path('delete/<int:id>/', views.deletePost),
]