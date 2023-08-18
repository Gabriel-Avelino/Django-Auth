from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
     path('cadastro/', views.cadastro, name='cadastro'),
     path('login/', views.login, name="login")
]