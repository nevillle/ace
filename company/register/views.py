from django.shortcuts import render
from rest_framework.views import APIView
from.serializers import *
from rest_framework.response import Response
# Create your views here.


class Register(APIView):

    def post(self,request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self,request):
        all_company = Company.objects.all()
        serializer = CompanySerializer(all_company, many=True)
        return Response(serializer.data)
