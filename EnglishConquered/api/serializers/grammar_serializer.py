from data.models import Grammar
from rest_framework import serializers

class GrammarSerializer(serializers.ModelSerializer):
    unit = serializers.CharField(source='module.unit')

    class Meta:
        model = Grammar
        fields = ('subject', 'content', 'unit')