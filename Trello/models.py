from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Auditable(models.Model):
    deleted = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    updated_at = models.DateTimeField(default=None, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name="+")

    class Meta:
        abstract = True
