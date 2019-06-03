from Servants.models import Servant
from rest_framework import serializers

class ServantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Servant
        fields = ('__all__')