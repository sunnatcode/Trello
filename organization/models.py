from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "organization"
