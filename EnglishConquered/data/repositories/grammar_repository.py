from data.models import Grammar

class GrammarRepository:
    def get_all(self):
        return Grammar.objects.filter(deleted_on__isnull=False).order_by('module__unit')

    def get(self, id):
        pass

    def add(self, grammar):
        pass

    def update(self, id, grammar):
        pass

    def delete(self, id):
        pass

