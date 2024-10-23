from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',user_signup),
    path('login/',user_login),
    path('verify/',verify_user),
    path('logout/',user_logout),
]