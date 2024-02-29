from rest_framework import serializers
from lists.models import ToDoList

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'