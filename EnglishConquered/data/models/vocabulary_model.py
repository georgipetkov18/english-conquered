from .module_model import Module
from .base_model import BaseEntity
from django.db import models

class Vocabulary(BaseEntity):

    class VocabularyType(models.TextChoices):
        WORD = 'Word'
        COLLOCATION = 'Collocation'
        PHRASAL_VERB = 'Phrasal verb'
        IDIOM = 'Idiom'

    content = models.CharField(null=False, max_length=256)
    description = models.CharField(null=False, max_length=1024)
    type = models.CharField(null=False, max_length=15, choices=VocabularyType.choices, default=VocabularyType.WORD)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)