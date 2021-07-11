from rest_framework import serializers
from .models import questions_db

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:

        model=questions_db
        #fields='__all__'
        fields=('id','name','question','company','year','similar_question')
