from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_todo, name='create_todo'),
    path('<int:todo_id>/toggle/', views.toggle_todo, name='toggle_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('list/', views.todo_list, name='todo_list'),  # Optional
]
