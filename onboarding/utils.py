from django.contrib.auth.models import User

def check_user(email):
    return User.objects.filter(email=email).exists()

def retrieve_token(req):
    auth_header = req.headers.get('Authorization',None)
    return auth_header