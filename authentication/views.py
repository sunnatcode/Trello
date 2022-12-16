from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as sign_out
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Trello.utils.mail_utils import send_activation_code
from Trello.utils.main_utils import store_file
from authentication.models import Employee, Token


def sign_in(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('landing:boards', user.username)
        messages.error(request, message='Username or password incorrect !', extra_tags="danger")
    return render(request, 'login.html', {})


@login_required
def logout(request):
    sign_out(request)
    redirect_url = reverse_lazy('auth:logged')
    return redirect(redirect_url)


def logged(request):
    return render(request, 'logged_out.html', {})


def sign_up(request):
    if request.POST:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if not password.__eq__(re_password):
            messages.error(request, 'Password does not match !', extra_tags="danger")
        else:
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),
                username=username,
                is_active=0
            )
            user.save()
            employee = Employee(phone_number=phone, user=user)
            file = request.FILES.get('file')
            file_id: int = store_file(file=file)
            employee.image_id = file_id
            employee.save()
            send_activation_code(user)
            return render(request, "sign_up_success_page.html", {"mail": user.email})

    return render(request, 'register.html', {})


def verify(request):
    token = request.GET.get('token')
    token = Token.objects.filter(token=token, deleted=0).first()
    if token:
        user = token.user
        user.is_active = 1
        user.save()
        token.deleted = 1
        token.save()
        return redirect('auth:verify_success_page')
    return HttpResponse("Token is invalid")


def verify_success_page(request):
    return render(request, 'verify_success_page.html', {})
