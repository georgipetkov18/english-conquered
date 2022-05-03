import uuid
from django.db import models

class BaseModel:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    class Meta:
        abstract=True