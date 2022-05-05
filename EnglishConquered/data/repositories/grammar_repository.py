from data.models import Grammar, Module
from business import models

class GrammarRepository:
    def get_all(self):
        return Grammar.objects.filter(deleted_on__isnull=True).order_by('module__unit')

    def get(self, id):
        grammar = Grammar.objects.filter(id=id)[0]
        if not grammar:
            raise Exception('Invalid id was provided')

        return grammar

    def add(self, grammar: models.Grammar):
        if grammar.subject == None or grammar.content == None or grammar.module <= 0:
            raise Exception('Invalid data was provided')

        module = Module.objects.filter(unit=grammar.module)
        if not module:
            raise Exception(f'Module of unit {grammar.module} does not exist')

        Grammar.objects.create(subject=grammar.subject, content=grammar.content, module=module[0])

    def update(self, id, grammar):
        pass

    def delete(self, id):
        pass

