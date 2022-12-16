from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from project.models import Project, ProjectColumn, ProjectMember
from task.models import Task, Comment


def projects(request):
    user = request.user
    list_project = Project.objects.filter(deleted=0, created_by_id=user)
    page = request.GET.get('page')
    paginator = Paginator(list_project, 9)
    try:
        list_project = paginator.page(page or 1)
    except EmptyPage:
        list_project = paginator.page(1)
    return render(request, "project_list.html", {"list_project": list_project})


@login_required
def project_create(request):
    if request.POST:
        name = request.POST["project_name"]
        deadline = request.POST["project_deadline"]
        if deadline:
            p = Project(name=name, deadline=deadline, created_by=request.user)
            p.save()
            return redirect("projects:project_detail", pk=p.id)
        else:
            project = Project(name=name, created_by=request.user)
            project.save()
            return redirect("projects:project_detail", pk=project.id)
    return render(request, "landing.html")


def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('projects:projects')


def project_update(request):
    return None


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    all_projects = Project.objects.filter(deleted=0, created_by_id=request.user)
    project_column = ProjectColumn.objects.filter(project_id=project.id)
    task = Task.objects.all()
    comments = Comment.objects.all()
    if request.POST:
        name = request.POST['column']
        if name:
            ProjectColumn(name=name, created_by=request.user, project_id=pk).save()
        else:
            messages.error(request, "Enter something!", extra_tags="danger")
    # else:
    #     search = request.GET["search"]
    #     if request.GET:
    #         member = User.objects.filter(username__contains=search)
    return render(request, "project_detail.html",
                  {"project": project, "all_projects": all_projects, 'tasks': task, 'project_column': project_column,
                   "user": request.user, 'comments': comments})


def column_delete(request, pk):
    column = ProjectColumn.objects.get(id=pk)
    project = column.project_id
    column.delete()
    return redirect('projects:project_detail', project)


def add_project_member(request, pk):
    if request.POST:
        emaill = request.POST['search']
        user = User.objects.filter(email=emaill).first()
        leader = request.POST['radio']
        if user:
            if leader:
                promember = ProjectMember(user_id=user.id, is_project_leader=leader, project_id=pk,
                                          created_by_id=request.user.id)
                promember.save()
            elif leader is False:
                promember = ProjectMember(user_id=user.id, project_id=pk, created_by_id=request.user.id)
                promember.save()
        else:
            messages.error(request, 'You must sign up', extra_tags='danger')
    return redirect('projects:project_detail', pk)
