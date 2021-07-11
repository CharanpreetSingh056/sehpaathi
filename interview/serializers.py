from rest_framework import serializers
from .models import interview_experiences_db

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:

        model=interview_experiences_db
        fields=('name','interview_experience','company','grad_year','course','id','date_of_upload')
