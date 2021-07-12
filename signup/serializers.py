from rest_framework import serializers
from .models import user_data, user_validation

class UserdataSerializer(serializers.ModelSerializer):
    class Meta:

        model=user_data
        fields='__all__'
class UserValidateSerializer(serializers.ModelSerializer):
    class Meta:

        model=user_validation
        fields='__all__'