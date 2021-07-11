from rest_framework import serializers
from .models import user_data

class UserdataSerializer(serializers.ModelSerializer):
    class Meta:

        model=user_data
        fields='__all__'