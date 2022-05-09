from django.http import JsonResponse
from rest_framework import status, views
from api.serializers.module_serializer import ModuleSerializer
from data.repositories import ModuleRepository
from business.models import Module

class ModuleView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.module_repo = ModuleRepository()


    def get(self, request, format=None):
        modules = self.module_repo.get_all()
        data = [ModuleSerializer(module).data for module in modules]
        return JsonResponse({'modules': data}, status=status.HTTP_200_OK)

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
        try:
            module = self.module_repo.get(id)
            return JsonResponse({'module': ModuleSerializer(module).data}, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, id, format=None):
        unit = request.data.get('unit')
        if unit == None:
            return JsonResponse({'error': 'The unit field is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            updated_module = self.module_repo.update(id, Module(unit))
            return JsonResponse({'updated_module': ModuleSerializer(updated_module).data}, status=status.HTTP_200_OK)
 
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id, format=None):
        try:
            self.module_repo.delete(id)
            return JsonResponse({'message': 'Module deleted successfully'}, status=status.HTTP_200_OK)
 
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        