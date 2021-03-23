from rest_framework import serializers
from .models import Endroits

class EndroitsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Endroits
        # fields=('description' , ......)
        fields= '__all__'