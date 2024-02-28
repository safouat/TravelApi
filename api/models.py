from django.db import models
import json
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    

class Traject(models.Model):
    userId=models.IntegerField(default=1)
    budget = models.CharField(max_length=100)  # Adjust max_length as needed
    ville = models.CharField(max_length=100)  # Adjust max_length as needed
    time = models.CharField(max_length=100)
    person_number = models.IntegerField()
    json_content = models.JSONField()
    def save(self, *args, **kwargs):
        # Serialize the JSON content before saving
        self.json_content = json.dumps(self.json_content)
        super().save(*args, **kwargs)

class Plan(models.Model):
        userId=models.IntegerField(default=1)
        json_content = models.JSONField()
        def save(self, *args, **kwargs):
        # Serialize the JSON content before saving
            self.json_content = json.dumps(self.json_content)
            super().save(*args, **kwargs)

class Match(models.Model):
     Date=models.DateField()
     Country1=models.CharField(max_length=100)
     Country2=models.CharField(max_length=100)

class Guider(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    ville= models.CharField(max_length=255)
     
     





        


