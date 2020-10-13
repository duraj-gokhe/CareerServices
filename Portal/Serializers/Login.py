from rest_framework import serializers
from Portal.models.Login import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'