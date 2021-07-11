from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from signup.models import user_data
from .models import rejection_reasons_db,rejection_reasons_comments_db
from .serializers import RejectionCommentsSerializer,RejectionReasonSerializer
from rest_framework import status

#get all reasons

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_all_reasons(request):
    all_reasons=rejection_reasons_db.objects.all().order_by('-time_of_upload')
    serializer=RejectionReasonSerializer(all_reasons,many=True)
    response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': reversed(serializer.data),
        }
    return Response(response)
# upload a new reason
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated,])
def upload_reason(request):
    if request.method=='GET':
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Return new_reason.html',
            }
        return Response(response)
    else:
        new_reason=rejection_reasons_db()
        if request.data['is_anonymous']==False:
            account=user_data.objects.get(email=request.user)
            new_reason.name=account.name
        new_reason.company=request.data['company']
        new_reason.reason=request.data['reason']
        new_reason.email=request.user
        new_reason.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Reason uploaded successfully.',
            }
        return Response(response)

#update a reason
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def update_reason(request,pk):

    try:
        reason_to_update=rejection_reasons_db.objects.get(id=pk)
        if str(request.user)!=reason_to_update.email:
            response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to update this since it was not uploaded by you.',
                }
            return Response(response)
        else:
            reason_to_update.reason=request.data['reason']
            reason_to_update.company=request.data['company']
            reason_to_update.save()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Reason updated successfully.',
                }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured, kindly try again later.',
                }
        return Response(response)

#Delete a reason
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,])
def delete_reason(request,pk):
    try:
        reason_to_delete=rejection_reasons_db.objects.get(id=pk)
        if str(request.user)!=reason_to_delete.email:
            response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'You are not permitted to delete this since it was not uploaded by you.',
                }
            return Response(response)
        else:
            reason_to_delete.delete()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Reason deleted successfully',
                }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured, kindly try again later.',
                }
        return Response(response)

#filter reasons
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def filter_reasons(request):
    company_list=request.data['list']
    try:

        if company_list is None:
            all_reasons=rejection_reasons_db.objects.all().order_by('-time_of_upload')
            serializer=RejectionReasonSerializer(all_reasons,many=True)
            response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': reversed(serializer.data),
            }
            return Response(response)
        else:
            filtered_reasons=rejection_reasons_db.filter(company__in=company_list)
            serializer=RejectionReasonSerializer(filtered_reasons,many=True)
            response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': reversed(serializer.data),
            }
            return Response(response)
    except:
        response = {
                'success' : 'False',
                'status code' : status.HTTP_400_BAD_REQUEST,
                'message': 'Some error occured, kindly try again later.',
                }
        return Response(response)

#add comment to reason
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def upload_comment(request,pk):
    try:
        comment_to=rejection_reasons_db.objects.get(id=pk)
        new_comment=rejection_reasons_comments_db()
        account=user_data.objects.get(email=comment_to.email)
        new_comment.name=account.name
        new_comment.email=account.email
        new_comment.reason=comment_to
        new_comment.comment=request.data['comment']
        new_comment.save()
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




