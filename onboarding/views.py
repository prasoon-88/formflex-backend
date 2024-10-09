from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import json
from .utils import check_user

@csrf_exempt
def user_signup(req):
    if req.method == "POST":
        body = json.loads(req.body)
        username = body.get('username',None)
        password = body.get('username',None)
        email = body.get('email',None)

        if username and email and password:
            if check_user(email):
                return JsonResponse({
                    'message':'user already registered',
                },status=400)

            user = User.objects.create(username=username,password=password,email=email)

            if user:
                return JsonResponse({
                    'message':'user created successfuly',
                    'email':email
                },status=201)
            else:
                return JsonResponse({
                    'message':'failed while create user',
                },status=400)
        return JsonResponse({
                    'message':'username ,email or password is invalid',
                },status=400)
    return JsonResponse({
                'message':'method not allowed',
        },status=405)


@csrf_exempt
def user_login(req):
    print('login')
    pass

@csrf_exempt
def user_logout(req):
    print('logout')
    pass
