from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from signup.models import user_data
from .models import general_questions_db,answers_db
from .serializers import GeneralQuestionSerializer,AnswerSerializer
from rest_framework import status

#get all questions
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_all_questions(request):
    all_questions=general_questions_db.objects.all()
    serializer=GeneralQuestionSerializer(all_questions,many=True)
    response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
    return Response(response)


# upload a new question
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated,])
def upload_question(request):
    if request.method=='GET':
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Return new_question.html',
            }
        return Response(response)

    else:
        new_question=general_questions_db()
        account=user_data.objects.get(email=request.user)
        new_question.name=account.name
        new_question.email=request.user
        new_question.question=request.data['question']
        new_question.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Question uploaded successfully.',
            }
        return Response(response)


#update a question
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def update_question(request,pk):
    question_to_update=general_questions_db.objects.get(id=pk)
    if str(request.user) != question_to_update.email:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to update this since it was not uploaded by you.',
                }
        return Response(response)

    else:
        question_to_update.question=request.data['question']
        question_to_update.save()
        response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Question updated successfully.',
                }
        return Response(response)


#delete a question
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,])
def delete_question(request,pk):
    question_to_delete=general_questions_db.objects.get(id=pk)
    if str(request.user) != question_to_delete.email:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to delete this since it was not uploaded by you.',
                }
        return Response(response)
    else:
        question_to_delete.delete()
        response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Question deleted successfully',
                }
        return Response(response)

#upload an answer
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def upload_answer(request,pk):
    try:
        answer_to=general_questions_db.objects.get(id=pk)
        new_answer=answers_db()
        account=user_data.objects.get(email=request.user)
        new_answer.question=answer_to
        new_answer.name=account.name
        new_answer.answer=request.data['answer']
        new_answer.email=account.email
        new_answer.save()
        response = {
                    'success' : 'True',
                    'status code' : status.HTTP_200_OK,
                    'message': 'Comment saved successfully.',
                    }
        return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured, kindly try again later.',
                }
        return Response(response)





