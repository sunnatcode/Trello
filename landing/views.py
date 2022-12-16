from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def boards(request, username):
    username = request.user
    return render(request, "landing.html", {"user": username})
