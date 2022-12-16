from django.urls import path
from project.views import (projects, add_project_member, project_create, project_delete, project_update, project_detail,
                           column_delete)

app_name = 'projects'
urlpatterns = [
    path("all", projects, name="projects"),
    path("project_detail/<int:pk>/", project_detail, name="project_detail"),
    path("project_create/", project_create, name="project_create"),
    path("project_delete/<int:pk>", project_delete, name="project_delete"),
    path("project_update/", project_update, name="project_update"),
    path("column_delete/<int:pk>/", column_delete, name="column_delete"),
    path("add_project_member/<int:pk>/", add_project_member, name="add_project_member")

]
