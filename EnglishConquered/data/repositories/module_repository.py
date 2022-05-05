from data.models import Module
from business import models

class ModuleRepository:
    def get_all(self):
        return Module.objects.filter(deleted_on__isnull=False).order_by('-unit')

    def get(self, id):
        module = Module.objects.filter(id=id)
        if not module:
            raise Exception('Invalid id was provided')

        return module

    def add(self, module: models.Module):
        if module.unit <= 0:
            raise Exception('Unit must be a positive integer')

        Module.objects.create(unit=module.unit)

    def update(self, id, module):
        pass

    def delete(self, id):
        pass