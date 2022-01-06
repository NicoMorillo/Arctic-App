from django.db import models

# Create your models here.

class Candidate(models.Model):
    name= models.CharField(max_length=20)
    candidate_ref= models.CharField(primary_key=True, max_length=8, unique=True)




class Scores(models.Model):
    score = models.FloatField(primary_key=True)
    candidate_ref= models.ForeignKey(Candidate, related_name='ref', on_delete=models.CASCADE)
   
