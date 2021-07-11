from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import interview_experiences_db
from signup.models import user_data
from .serializers import InterviewSerializer
from rest_framework import status


#get all interview experiences
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def interview_experiences(request):
    all_interviews=interview_experiences_db.objects.all()
    serializer=InterviewSerializer(all_interviews,many=True)
    response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
    return Response(response)

#post new_interview experience

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,])
def new_interview_experience(request):
    if request.method=='GET':
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Return new_interview_experience.html',
            }
        return Response(response)
    else:
        body=request.data['body']
        company=request.data['company']
        email=request.user
        try:
            account=user_data.objects.get(email=email)
            new_interview=interview_experiences_db()
            new_interview.name=account.name
            new_interview.email=email
            new_interview.interview_experience=body
            new_interview.company=company
            new_interview.grad_year=account.grad_year
            new_interview.course=account.course
            new_interview.save()
            response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Interview Experience uploaded successfully',
            }
            return Response(response)

        except:
            response = {
            'success' : 'False',
            'status code' : status.HTTP_400_BAD_REQUEST,
            'message': 'Some error ocured.',
            }
            return Response(response)

# delete an interview_experience
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,])
def delete_interview_experience(request,pk):

    try:
        interview_experience=interview_experiences_db.objects.get(id=pk)
        user=str(request.user)
        if user!=interview_experience.email:
            response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to delete this since it was not uploaded by you.',
                }
        else:
            interview_experience.delete()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Interview Experience deleted successfully',
                }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured while deleting this Interview Experience.',
                }
        return Response(response)

#update ke lie
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def update_interview_experience(request,pk):
    try:
        interview_experience=interview_experiences_db.objects.get(id=pk)
        user=str(request.user) # since its type is model.
        if interview_experience.email!=user:
            response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to delete this since it was not uploaded by you.',
                }
            return Response(response)
        else:

            interview_experience.body=request.data['body']
            interview_experience.company=request.data['company']
            interview_experience.save()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Interview Experience updated successfully',
                }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured while updating this Interview Experience.',
                }
        return Response(response)

#filter acc to company
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def filter_interview_experiences(request):
    company_list=request.data['list']
    if company_list is not None:
        all_interviews=interview_experiences_db.objects.filter(company__in=company_list)
        serializer=InterviewSerializer(all_interviews,many=True)
        response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
        return Response(response)

    else:
        all_interviews=interview_experiences_db.objects.all()
        serializer=InterviewSerializer(all_interviews,many=True)
        response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
        return Response(response)


