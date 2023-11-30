from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class TaskListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(CreateAPIView):
    permission_classes=[AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        status_data = request.data.get('status')
        if status_data is not None:
            instance.status = status_data
            instance.save()

        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
