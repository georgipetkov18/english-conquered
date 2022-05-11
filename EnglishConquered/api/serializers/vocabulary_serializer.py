from data.models import Vocabulary
from rest_framework import serializers

class VocabularySerializer(serializers.ModelSerializer):
    unit = serializers.CharField(source='module.unit')

    class Meta:
        model = Vocabulary
        fields = ('content', 'description', 'type', 'unit')