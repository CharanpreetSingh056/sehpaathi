from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import questions_db
from .serializers import QuestionsSerializer
from signup.models import user_data
from rest_framework import status



# Create your views here.
# returns home page
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def homepage(request):
    response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Return home.html',
                }
    return Response(response)


#returns questions page

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_questions(request):
    all_questions=questions_db.objects.all()
    serializer=QuestionsSerializer(all_questions,many=True)
    response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
    return Response(response)

#add a new question
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,])
def new_question(request):
    if request.method=='GET':

        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Return new_question.html',
            }
        return Response(response)

    else :
        email=request.user
        user_profile=user_data.objects.get(email=email)
        name=user_profile.name
        temp_data=request.data
        new_ques=questions_db(name=name,email=email,question=request.data['question'],company=request.data['company'],year=request.data['year'],similar_question=request.data['similar_question'])
        new_ques.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Question uploaded successfully',
            }
        return Response(response)

# to delete a question
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_question(request,pk):
    try:
        question=questions_db.objects.get(id=pk)
        user=str(request.user) # since its type is model.
        if question.email!=user:
            response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to delete this since it was not uploaded by you.',
                }
            return Response(response)
        else:
            question.delete()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Question deleted successfully',
                }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured while deleting this question.',
                }
        return Response(response)

# to update question
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def update_question(request,pk):
    try:
        question=questions_db.objects.get(id=pk)
        user=str(request.user) # since its type is model.
        if question.email!=user:
            response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to update this since it was not uploaded by you.',
                }
            return Response(response)
        else:

            question.question=request.data['question']
            question.company=request.data['company']
            question.year=request.data['year']
            question.similar_question=request.data['similar_question']
            question.save()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Question updated successfully',
                }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured while updating this question.',
                }
        return Response(response)

# filter questions according to company
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def filter_questions(request):
    company_list=request.data['list']
    if len(company_list) == 0:
        all_questions=questions_db.objects.all()
        serializer=QuestionsSerializer(all_questions,many=True)
        response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
    return Response(response)
    all_questions=questions_db.objects.filter(company__in=company_list)
    serializer=QuestionsSerializer(all_questions,many=True)
    response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
    return Response(response)