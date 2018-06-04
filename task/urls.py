from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('completed/<todo_id>', views.completed, name='completed' ),
    path('delete/', views.delete, name='delete'),
]