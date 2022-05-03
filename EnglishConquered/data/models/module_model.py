from .base_model import BaseEntity
from django.db import models

class Module(BaseEntity):
    unit = models.IntegerField(null=False)