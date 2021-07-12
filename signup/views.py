from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import UserdataSerializer
from .models import user_data,User,user_validation,user_forgot_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
import os
from decouple import config
import string
import random
from django.contrib.auth.hashers import make_password
from validate_email import validate_email

# Create your views here.
def to_send_mail(token,email,current_site):
    return


def send_email_passwordchange(token,email,current_site):

    email_subject='Confirm your password change.'
    to_email=email
    from_email=settings.EMAIL_HOST_USER
    current_site=current_site+'/forgot_password_validate/'
    current_site=current_site+token+'/'
    message='Hello, in order to reset your password, click on this link '+current_site
    send_mail(email_subject,message,from_email,[to_email,])


@api_view(['GET'])
@permission_classes([AllowAny,])
def signup_page(request):
    response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Return signup.html',
            }
    return Response(response)


@api_view(['GET','POST'])
@permission_classes([AllowAny,])
def signup_data(request):
    if request.method=='GET':
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Return signup.html',
            }
        return Response(response)
    else:
        serializer=UserdataSerializer(data=request.data)
        # check if it is an iiitl email.
        is_valid = validate_email(email_address=request.data['email'], check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10, check_smtp=True, smtp_timeout=10, smtp_helo_host='my.host.name', smtp_from_address='my@from.addr.ess', smtp_debug=False)
        print(is_valid)
        if is_valid==False:
            response = {
            'success' : 'False',
            'status code' : status.HTTP_400_BAD_REQUEST,
            'message': 'Invalid E-mail address, kindly chek your E-mail address and try again.',
            }
            return Response(response)
        try:
            accounts=user_data.objects.get(email=request.data['email']) #user data mei save hi tabhi krwaaunga jab activate link confirm ho jaaegi.
            response = {
            'success' : 'False',
            'status code' : status.HTTP_400_BAD_REQUEST,
            'message': 'You have already signed in using this E-mail, try to log in or try signing up with another valid E-mail',
            }
            return Response(response)
        except:
            try:
                try:
                    does_exist=user_validation.objects.get(email=request.data['email'])
                    if does_exist is not None:
                        random_string=does_exist.token
                        current_site='/'+str(get_current_site(request))
                        to_send_mail(does_exist.token,request.data['email'],current_site)
                        response = {
                        'success' : 'True',
                        'status code' : status.HTTP_200_OK,
                        'message': 'Check your E-mail to complete the signup.',
                        }
                        return Response(response)

                except:
                    all_chars=string.ascii_letters + string.digits
                    random_string=''.join(random.choices(all_chars, k=20))
                    current_site='/'+str(get_current_site(request))
                    email_subject='Activate your account'
                    email=request.data['email']
                    to_email=email
                    return Response("Reached here")
                    from_email=settings.EMAIL_HOST_USER
                    current_site=current_site+'/validation/'
                    current_site=current_site+token+'/'
                    message='Hello, in order to activate your account, click on this link '+current_site
                    send_mail(email_subject,message,from_email,[to_email,])
                    #to_send_mail(random_string,request.data['email'],current_site)
                    new_validation=user_validation(name=request.data['name'],email=request.data['email'],phone=request.data['phone'],password=request.data['password'],grad_year=request.data['grad_year'],course=request.data['course'],token=random_string)
                    new_validation.save()

                    response = {
                        'success' : 'True',
                        'status code' : status.HTTP_200_OK,
                        'message': 'Check your E-mail to complete the signup.',
                        }
                    return Response(response)

            except:
                response = {
                        'success' : 'False',
                        'status code' : status.HTTP_400_BAD_REQUEST,
                        'message': 'Some error occured while signing up, please try again later.',
                        }
                return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def getall(request):
    accounts=user_data.objects.all()
    serializer=UserdataSerializer(accounts,many=True) # Jab bhi object pass krna ho to iss tareeke se karenge, aur list pass karni ho to data=request.data se
    return Response(serializer.data)

#validation of user email
@api_view(['GET'])
@permission_classes([AllowAny,])
def validate(request,token):
    try:
        user_to_validate=user_validation.objects.get(token=token)
        if token==user_to_validate.token:
            new_user=User.objects.create_user(user_to_validate.email,user_to_validate.password)
            new_user.save()
            new_user_data=user_data(name=user_to_validate.name,email=user_to_validate.email,phone=user_to_validate.phone,password=user_to_validate.password,grad_year=user_to_validate.grad_year,course=user_to_validate.course)
            new_user_data.save()
            user_to_validate.delete()
            response = {
                        'success' : 'True',
                        'status code' : status.HTTP_200_OK,
                        'message': 'Signup successful, login now to access your account.',
                        }
            return Response(response)
        else:
            response = {
                        'success' : 'False',
                        'status code' : status.HTTP_400_BAD_REQUEST,
                        'message': 'Token expired, try to sign in again.',
                        }
            return Response(response)
    except:
        response = {
                        'success' : 'False',
                        'status code' : status.HTTP_400_BAD_REQUEST,
                        'message': 'Some error in creating user, probably the link is expired, try signing in again.',
                        }
        return Response(response)

#forgot password and to send mail for the same.
@api_view(['POST','GET'])
@permission_classes([AllowAny,])
def forgot_password(request):
    if request.method=='GET':
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Render forgot password.html',
            }
        return Response(response)
    else:
        email=request.data['email']
        new_password=request.data['password']
        try:

            account_user_data=user_data.objects.get(email=email) # agar already signed up nhi hoga to yahi pe break
            try:
                does_exist=user_forgot_password.objects.get(email=email)
                if does_exist is not None:
                    random_string=does_exist.token
                    current_site='/'+str(get_current_site(request))
                    send_email_passwordchange(random_string,email,current_site)
                    response = {
                    'success' : 'True',
                    'status code' : status.HTTP_200_OK,
                    'message': 'Check your E-mail to confirm the password change.',
                    }
                    return Response(response)
            except:
                all_chars=string.ascii_letters + string.digits
                random_string=''.join(random.choices(all_chars, k=20))
                current_site='/'+str(get_current_site(request))
                send_email_passwordchange(random_string,email,current_site)
                new_password_change=user_forgot_password(email=email,password=new_password,token=random_string)
                new_password_change.save()
                response = {
                    'success' : 'True',
                    'status code' : status.HTTP_200_OK,
                    'message': 'Check your E-mail to confirm the password change.',
                    }
                return Response(response)

        except:
            response = {
            'success' : 'True',
            'status code' : status.HTTP_400_BAD_REQUEST,
            'message': 'User with given E-mail does not exist.',
            }
            return Response(response)

# to validate the password change
@api_view(['GET'])
@permission_classes([AllowAny,])
def forgot_password_validate(request,token):
    try:
        to_change=user_forgot_password.objects.get(token=token)
        if to_change.token==token:
            account_user_data=user_data.objects.get(email=to_change.email)
            account_User=User.objects.get(email=to_change.email)
            account_user_data.password=to_change.password
            account_User.password=make_password(to_change.password) #for encrpypting the password
            account_User.save()
            account_user_data.save()
            to_change.delete()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Password changed successfully.',
                }
            return Response(response)
    except:
        response = {
            'success' : 'True',
            'status code' : status.HTTP_400_BAD_REQUEST,
            'message': 'Some error in changing the password, kindly try again later',
            }
        return Response(response)

