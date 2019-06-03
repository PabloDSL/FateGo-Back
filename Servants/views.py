from Servants.models import Servant
from Servants.serializers import ServantSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import JSONParser

# Create your views here.
class ServantList(APIView):
    queryset = Servant.objects.all()
    def get(self,request,format=None):
       queryset = Servant.objects.all()
       serializer = ServantSerializer(queryset,many=True)
       return Response(serializer.data)

    def post(self, request, format = None):
       serializer = ServantSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           datas = serializer.data
           response = datas
           return Response(response,status=status.HTTP_201_CREATED)  
       response = serializer.errors
       return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        data = request.data
        servant = Servant.objects.get(id=pk)
        serializer = ServantSerializer(servant, data=data)
        if serializer.is_valid():
            servantUpdated = serializer.save()
            return servantUpdated
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk,format=None):
        # Get object with this pk
        servant = get_object_or_404(Servant.objects.all(), pk=pk)
        respuesta = Servant.objects.get(id=pk)
        print("respuesta: ",respuesta)
        servant.delete()
        return {'id':respuesta[0], 'Nombre':respuesta[1],'Clase':respuesta[2], 'Deck': respuesta[3], 'noblePhantasm':respuesta[4] }