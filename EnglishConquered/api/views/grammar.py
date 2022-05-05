from django.http import JsonResponse
from rest_framework import status, views
from api.serializers import GrammarSerializer
from data.repositories import GrammarRepository
from business.models import Grammar

class GrammarView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grammar_repo = GrammarRepository()

    def get(self, request, format=None):
        grammars = self.grammar_repo.get_all()
        data = [GrammarSerializer(grammar).data for grammar in grammars]
        return JsonResponse({'grammars': data}, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        subject = request.data.get('subject')
        content = request.data.get('content')
        unit = request.data.get('unit')

        if subject == None or content == None or unit == None:
            return JsonResponse({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            grammar = Grammar(subject, content, unit)
            self.grammar_repo.add(grammar)
            return JsonResponse({'message': 'Grammar created successfully'}, status=status.HTTP_201_CREATED)


        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GrammarDetailView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grammar_repo = GrammarRepository()

    def get(self, request, id, format=None):
        try:
            grammar = self.grammar_repo.get(id)
            return JsonResponse({'grammar': GrammarSerializer(grammar).data}, status=status.HTTP_200_OK)


        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        