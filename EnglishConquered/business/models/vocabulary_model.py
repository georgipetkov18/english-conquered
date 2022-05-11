from data.choices import VocabularyType

class Vocabulary:
    def __init__(self, content: str, description: str, type: str, module: int):
        self.content = content
        self.description = description
        self.module = module
        if type not in VocabularyType.values:
            raise Exception('Invalid vocabulary type was provided')
        self.type = type