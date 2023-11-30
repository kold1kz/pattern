from rest_framework import serializers
from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    '''serializer task'''
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Status'] = representation['status']
        del representation['status']
        return representation

    def create(self, validated_data):
        status = validated_data.pop('Status', 'в процессе')
        task = Task.objects.create(status=status, **validated_data)
        return task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('Status', instance.status)
        instance.save()
        return instance