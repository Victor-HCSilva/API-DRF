from django.urls import path
from . import views

urlpatterns = [
    path('api/list/', views.TodoListView.as_view(), name='todo-list'),
    path('api/list/<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
]