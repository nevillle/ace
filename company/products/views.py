from django.shortcuts import render
from rest_framework.views import APIView
from.serializers import *
from rest_framework.response import Response
from register.models import Company
# Create your views here.


class AddProduct(APIView):

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GetProducts(APIView):

    def get(self,request,company_id):
        comapny = Company.objects.get(id=company_id)
        all_products = Product.objects.filter(comapny=comapny)
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)