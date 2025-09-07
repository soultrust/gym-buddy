from rest_framework import viewsets 
from .serializers import ExerciseSerializer 
from .models import Exercise 
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated 

class ExerciseViewSet(viewsets.ModelViewSet):
  serializer_class = ExerciseSerializer
  queryset = Exercise.objects.all() 
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,) 