from data.models import Module
from business import models

class ModuleRepository:
    def get_all(self):
        return Module.objects.filter(deleted_on__isnull=True).order_by('-unit')


    def get(self, id):
        module = Module.objects.filter(id=id)[0]
        if not module:
            raise Exception('Invalid id was provided')

        return module


    def add(self, module: models.Module):
        if module.unit <= 0:
            raise Exception('Unit must be a positive integer')

        Module.objects.create(unit=module.unit)


    def update(self, id, module: models.Module):
        if module.unit <= 0:
            raise Exception('Unit must be a positive integer')

        Module.objects.filter(id=id).update(unit=module.unit)
        return Module.objects.filter(id=id)[0]


    def delete(self, id):
        Module.objects.filter(id=id).delete()

