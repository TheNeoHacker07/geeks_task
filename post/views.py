from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView

from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer


class ListTodo(ListAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer


class RetrieveTodo(RetrieveAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='pk'

class CreateTodo(CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class DeleteTodo(DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='pk'


class UpdateTodo(UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='pk'












# Create you views here.
