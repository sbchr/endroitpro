from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Endroits
from .serializers import EndroitsSerializer

# Create your views here.

class EndroitsList(APIView):

    def get(self, request):
        Endroits1= Endroits.objects.all()
        serializer= EndroitsSerializer(Endroits1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
