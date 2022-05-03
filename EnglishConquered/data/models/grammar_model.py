from .base_model import BaseEntity
from .module_model import Module

from django.db import models

class Grammar(BaseEntity):
    subject = models.CharField(null=False, max_length=256)
    content = models.CharField(null=False, max_length=1024)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)