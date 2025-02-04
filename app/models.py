from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

class TodoList(models.Model):
    tarefa = models.CharField(max_length=200)
    categoria = models.IntegerField()
    concluido = models.BooleanField(default=False)

    def __str__(self):
         return self.tarefa