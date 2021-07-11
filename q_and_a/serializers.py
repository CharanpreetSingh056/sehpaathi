from rest_framework import serializers
from .models import general_questions_db,answers_db

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=answers_db
        fields=('id','name','question','answer','time_of_upload')

class GeneralQuestionSerializer(serializers.ModelSerializer):
    answer=AnswerSerializer(many=True,read_only=True)
    class Meta:
        model=general_questions_db
        fields=('id','name','time_of_upload','question','answer')