from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
import json
from .utils import check_user,retrieve_token

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

            user = User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()

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
    if req.method == 'POST':
        body = json.loads(req.body)
        email = body.get('email',None)
        password = body.get('password',None)

        if email and password:
            try:
                user = User.objects.get(email=email)
                if user is None or user.check_password(password) is None:
                    return JsonResponse({
                        "message":"email or password is invalid"
                    },status=400)

            except User.DoesNotExist:
                return JsonResponse({
                        "message":"user does not exists"
                    },status=400)

            login(request=req,user=user)
            refresh_token = RefreshToken.for_user(user)
            return JsonResponse({
                        "message":"success",
                        "refreshToken":str(refresh_token),
                        "accessToken":str(refresh_token.access_token)
                    },status=200)
            
        return JsonResponse({
                "message":"email and password is mandatory"
            },status=400)
    return JsonResponse({
        "message":"method not allowed"
    },status=405)

@csrf_exempt
def verify_user(req):
    if req.method == 'GET':
        token = retrieve_token(req) 
        try:
            access_token_obj = AccessToken(token)
            user_id = access_token_obj['user_id']
            user = User.objects.get(id=user_id)
            if user:
                return JsonResponse({"message":'done'},status=200)
        except:
            return JsonResponse({
                    "message":"something went wrong"
                },status=500)
        return JsonResponse({
                    "message":"unauthorized"
                },status=401)
    return JsonResponse({
        "message":"method not allowed"
    },status=405)

@csrf_exempt
def user_logout(req):
    if req.method == "POST":
        if req.user.is_authenticated:
            logout(request=req)
            try:
                refresh_token = retrieve_token(req)
                token = RefreshToken(refresh_token)
                token.blacklist()
            except:
                print('Error during token blacklisting while logout')
            return JsonResponse({
                "message":"success"
            },status=200)
        return JsonResponse({
                "message":"user is not logged in"
            },status=400)
    return JsonResponse({
        "message":"method not allowed"
    },status=405)
