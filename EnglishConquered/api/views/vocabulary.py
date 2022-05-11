from django.http import JsonResponse
from rest_framework import status, views
from api.serializers import VocabularySerializer
from data.repositories import VocabularyRepository
from business.models import Vocabulary

class VocabularyView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vocabulary_repo = VocabularyRepository()

    
    def get(self, request, format=None):
        vocabularies = self.vocabulary_repo.get_all()
        data = [VocabularySerializer(vocabulary).data for vocabulary in vocabularies]
        return JsonResponse({'vocabulary': data}, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        content = request.data.get('content')
        description = request.data.get('description')
        type = request.data.get('type')
        unit = request.data.get('unit')

        if content == None or description == None or type == None or unit == None:
            return JsonResponse({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            vocabulary = Vocabulary(content, description, type, unit)
            self.vocabulary_repo.add(vocabulary)
            return JsonResponse({'message': 'Vocabulary created successfully'}, status=status.HTTP_201_CREATED)


        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VocabularyDetailView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vocabulary_repo = VocabularyRepository()

    
    def get(self, request, id, format=None):
        print('maikati shte eba')
        try:
            vocabulary = self.vocabulary_repo.get(id)
            print(vocabulary)
            return JsonResponse({'vocabulary': VocabularySerializer(vocabulary).data}, status=status.HTTP_200_OK)


        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id, format=None):
        content = request.data.get('content')
        description = request.data.get('description')
        type = request.data.get('type')
        unit = request.data.get('unit')

        if content == None or description == None or type == None or unit == None:
            return JsonResponse({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            updated_vocabulary = self.vocabulary_repo.update(id, Vocabulary(content, description, type, unit))
            return JsonResponse({'updated_vocabulary': VocabularySerializer(updated_vocabulary).data}, status=status.HTTP_200_OK)
 
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        try:
            self.vocabulary_repo.delete(id)
            return JsonResponse({'message': 'Vocabulary deleted successfully'}, status=status.HTTP_200_OK)
 
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)