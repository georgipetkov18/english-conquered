from django.db import models

class VocabularyType(models.TextChoices):
        WORD = 'word'
        COLLOCATION = 'collocation'
        PHRASAL_VERB = 'phrasal verb'
        IDIOM = 'idiom'