from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',user_signup),
    path('login/',user_login),
    path('logout/',user_logout),
]