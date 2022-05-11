from data.models import Vocabulary, Module
from business import models

class VocabularyRepository:
    def get_all(self):
        return Vocabulary.objects.filter(deleted_on__isnull=True).order_by('module__unit')


    def get(self, id):
        vocabularies = Vocabulary.objects.filter(id=id)
        if not vocabularies:
            raise Exception('Invalid id was provided')

        return vocabularies[0]


    def add(self, vocabulary: models.Vocabulary):
        if vocabulary.content == None or vocabulary.description == None or vocabulary.type == None or vocabulary.module <= 0:
            raise Exception('Invalid data was provided')

        modules = Module.objects.filter(unit=vocabulary.module)
        if not modules:
            raise Exception(f'Module of unit {vocabulary.module} does not exist')
        Vocabulary.objects.create(content=vocabulary.content, description=vocabulary.description, type=vocabulary.type, module=modules[0])


    def update(self, id, vocabulary: models.Vocabulary):
        if vocabulary.module <= 0:
            raise Exception('Module must be a positive integer')

        modules = Module.objects.filter(unit=vocabulary.module)
        if not modules:
            raise Exception(f'Module of unit {vocabulary.module} does not exist')

        vocabularies = Vocabulary.objects.filter(id=id)
        if not vocabularies:
            raise Exception('Invalid id was provided')

        vocabularies.update(content=vocabulary.content, description=vocabulary.description, type=vocabulary.type, module=modules[0])
        return Vocabulary.objects.filter(id=id)[0]


    def delete(self, id):
        vocabularies = Vocabulary.objects.filter(id=id)
        if not vocabularies:
            raise Exception('Invalid id was provided')

        vocabularies.delete()


