from rest_framework import generics
from .models import TodoList
from .serializers import TodoListSerializer

class TodoListView(generics.ListCreateAPIView):
    queryset = TodoList.objects.all() # Remova o filtro .filter(user=...)
    serializer_class = TodoListSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all() # Remova o filtro .filter(user=...)
    serializer_class = TodoListSerializer
    lookup_field = 'pk'