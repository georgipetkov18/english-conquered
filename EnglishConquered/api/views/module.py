from django.http import JsonResponse
from rest_framework import status, views
from data.repositories import ModuleRepository
from business.models import Module

class ModuleView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.module_repo = ModuleRepository()

    def post(self, request, format=None):
        unit = request.data.get('unit')
        if unit == None:
            return JsonResponse({'error': 'The unit field is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            module = Module(unit)
            self.module_repo.add(module)
            return JsonResponse({'message': 'Module created successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ModuleDetailView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.module_repo = ModuleRepository()

    def get(self, request, id, format=None):
        pass