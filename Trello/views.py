from django.shortcuts import render, redirect


def home_page(request):
    if request.user.is_authenticated:
        return redirect("landing:boards", request.user.username)
    return render(request, 'home.html', {})
