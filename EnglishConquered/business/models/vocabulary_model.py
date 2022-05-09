from data.choices import VocabularyType

class Vocabulary:
    def __init__(self, content: str, description: str, type: VocabularyType, module: int):
        self.content = content
        self.description = description
        self.type = type,
        self.module = module