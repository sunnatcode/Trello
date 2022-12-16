from django.urls import path
from .views import boards

app_name = 'landing'
urlpatterns = [
    path('<str:username>/boards', boards, name='boards'),
]
