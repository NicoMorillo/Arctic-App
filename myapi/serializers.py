from rest_framework import serializers
from .models import Candidate, Scores

class ScoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Scores
        fields = ('score','candidate_ref')

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    ref = ScoresSerializer(many=True, read_only=True)
    class Meta:
        model= Candidate
        fields = ('name','candidate_ref')