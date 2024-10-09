from django.contrib.auth.models import User

def check_user(email):
    return User.objects.filter(email=email).exists()

    