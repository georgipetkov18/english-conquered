from data.models import Grammar, Module
from business import models

class GrammarRepository:
    def get_all(self):
        return Grammar.objects.filter(deleted_on__isnull=True).order_by('module__unit')


    def get(self, id):
        grammars = Grammar.objects.filter(id=id)
        if not grammars:
            raise Exception('Invalid id was provided')

        return grammars[0]


    def add(self, grammar: models.Grammar):
        if grammar.subject == None or grammar.content == None or grammar.module <= 0:
            raise Exception('Invalid data was provided')

        modules = Module.objects.filter(unit=grammar.module)
        if not modules:
            raise Exception(f'Module of unit {grammar.module} does not exist')

        Grammar.objects.create(subject=grammar.subject, content=grammar.content, module=modules[0])


    def update(self, id, grammar: models.Grammar):
        if grammar.module <= 0:
            raise Exception('Module must be a positive integer')

        modules = Module.objects.filter(unit=grammar.module)
        if not modules:
            raise Exception(f'Module of unit {grammar.module} does not exist')

        grammars = Grammar.objects.filter(id=id)
        if not grammars:
            raise Exception('Invalid id was provided')

        grammars.update(subject=grammar.subject, content=grammar.content, module=modules[0])
        return Grammar.objects.filter(id=id)[0]


    def delete(self, id):
        grammars = Grammar.objects.filter(id=id)
        if not grammars:
            raise Exception('Invalid id was provided')

        grammars.delete()


