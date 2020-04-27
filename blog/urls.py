from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('newpost/', views.newpost, name='newpost'),
    path('editpost/<int:post_id>', views.editpost, name='editpost'),
    path('addpost/', views.addpost, name='addpost'),
]