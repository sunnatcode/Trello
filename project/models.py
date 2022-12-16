from django.contrib.auth.models import User
from django.db import models

from Trello.models import Auditable


class Project(Auditable):
    name = models.CharField(max_length=50, unique=True)
    closed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True)

    class Meta:
        db_table = "project"


class ProjectColumn(Auditable):
    name = models.CharField(max_length=255)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    order = models.SmallIntegerField(default=1)

    class Meta:
        db_table = "project_column"


class ProjectMember(Auditable):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    is_project_leader = models.BooleanField(default=False)

    class Meta:
        db_table = "project_member"



