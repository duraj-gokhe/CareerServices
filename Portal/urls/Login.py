from django.urls import path
from Portal.views import Login

urlpatterns = [
    path('login',Login.login, name='person_login'),
]