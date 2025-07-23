from django.db import models
from django.contrib.auth.models import User 

class Exercise(models.Model): 
  title = models.CharField(max_length=32)
