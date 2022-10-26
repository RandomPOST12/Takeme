from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from django.http import JsonResponse

from app.serializers import DataSerializer
from .models import Data
# Create your views here.

class Home(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


        
        
