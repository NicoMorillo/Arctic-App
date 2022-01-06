from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CandidateSerializer, ScoresSerializer
from .models import Candidate, Scores

# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class ScoresViewSet(viewsets.ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoresSerializer()
