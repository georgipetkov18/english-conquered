from django.db import models

class VocabularyType(models.TextChoices):
        WORD = 'Word'
        COLLOCATION = 'Collocation'
        PHRASAL_VERB = 'Phrasal verb'
        IDIOM = 'Idiom'