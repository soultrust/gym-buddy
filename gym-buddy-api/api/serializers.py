from rest_framework import serializers 
from .models import Exercise, Set

class SetSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Set 
    fields = ['id', 'weight', 'reps', 'entrydate']

class ExerciseSerializer(serializers.ModelSerializer):
  sets = SetSerializer(many=True)
  
  class Meta:
    model = Exercise
    fields = ['id', 'title', 'sets']

