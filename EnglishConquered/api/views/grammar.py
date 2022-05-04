from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import GrammarSerializer
from data.repositories import GrammarRepository

@api_view(['GET'])
def get_grammars(request, format=None):
    grammar_repo = GrammarRepository()
    grammars = grammar_repo.get_all()
    data = [GrammarSerializer(grammar).data for grammar in grammars]
    return JsonResponse({'grammars': data}, status=status.HTTP_200_OK)