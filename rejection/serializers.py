from rest_framework import serializers
from .models import rejection_reasons_comments_db,rejection_reasons_db

class RejectionCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=rejection_reasons_comments_db
        fields=('name','comment','reason','time_of_upload')


class RejectionReasonSerializer(serializers.ModelSerializer):
    comment=RejectionCommentsSerializer(read_only=True,many=True)
    class Meta:
        model=rejection_reasons_db
        fields=('name','id','time_of_upload','company','reason','comment')

