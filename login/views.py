from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from signup.models import user_data
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from signup.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny,])
def login(request):
    response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Return login.html',
                }
    return Response(response)

#logout
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def logout(request):
    r_token=request.data["refresh"]
    token=RefreshToken(r_token)
    try:
        token.blacklist()
        response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Successfully logged out.',
                }
        return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error in logging out the user.',
                }
        return Response(response)

#change password
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def change_password(request):
    old_password=request.data['old_password']
    new_password=request.data['new_password']
    try:
        account=user_data.objects.get(email=request.user)
        if account.password != old_password:
            response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Wrong password, try chaning your password again.',
                }
            return Response(response)
        else :

            user=User.objects.get(email=request.user)
            account.password=new_password
            user.password=make_password(new_password) # for encrypting the password.
            account.save()
            user.save()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Password changed successfully.',
                }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured, kindly try again later.',
                }
        return Response(response)
