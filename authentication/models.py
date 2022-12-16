from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from organization.models import Organization


class Uploads(models.Model):
    original_name = models.CharField(max_length=300)
    content_type = models.CharField(max_length=100)
    new_name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    code = models.CharField(max_length=70, unique=True)
    size = models.IntegerField()

    class Meta:
        db_table = 'uploads'


class Employee(models.Model):
    image = models.OneToOneField(Uploads, on_delete=CASCADE)
    phone_number = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=CASCADE, null=True)
    organization = models.OneToOneField(Organization, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'auth_employee'


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'token'
