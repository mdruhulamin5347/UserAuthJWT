from rest_framework import serializers
from .models import *

class first_serializer(serializers.ModelSerializer):
    class Meta:
        model = frist_model
        fields = '__all__'
    
class second_serializer(serializers.ModelSerializer):
    class Meta:
        model = second_model
        fields = '__all__'
    
class thirth_serializer(serializers.ModelSerializer):
    class Meta:
        model = thirth_model
        # fields='__all__'
        exclude=('user',)
    
class fourth_serializer(serializers.ModelSerializer):
    class Meta:
        model = fourth_model
        # fields='__all__'
        exclude=('user','create_at')