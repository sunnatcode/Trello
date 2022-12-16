from django.urls import path
from authentication.views import (
    sign_in, logout, logged, sign_up, verify, verify_success_page
)

app_name = 'auth'
urlpatterns = [
    path('login/', sign_in, name='signin'),
    path('sign_up/', sign_up, name='sign_up'),
    path('logout/', logout, name='logout'),
    path('logged/', logged, name='logged'),
    path('verify/', verify, name='verify'),
    path('verify_success_page/', verify_success_page, name='verify_success_page'),
]
