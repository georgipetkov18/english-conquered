from data.models import Grammar
from rest_framework import serializers

class GrammarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grammar
        fields =('subject', 'content', 'module')