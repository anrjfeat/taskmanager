from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    description=serializers.CharField(max_length=50)
    email=serializers.CharField(max_length=254)
    createdAt=serializers.DateTimeField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)