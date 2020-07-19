from django.shortcuts import render
from rest_framework.views import APIView
from.serializers import *
from rest_framework.response import Response
from register.models import Company
from products.models import Product
import datetime
import decimal
# Create your views here.


class CreatePurchaseOrder(APIView):

    def post(self,request):
        data = {}
        comapny_id = request.data['company']
        product_id =  request.data['product']
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            error_msg  =[]
            error_msg.append('Wrong product id ')
            return Response({'error':error_msg})
        try:
            comapny = Company.objects.get(id=comapny_id)
        except Company.DoesNotExist:
            error_msg  =[]
            error_msg.append('Wrong Company id ')
            return Response({'error':error_msg})
        if product.comapny.id != comapny.id:
            error_msg = []
            error_msg.append('product and company does not match')
            return Response({'error': error_msg})
        data['product'] = product.id
        data['comapny'] = comapny.id
        data['date']=datetime.date.today()
        data['qty'] = request.data['qty']
        data['total_cost'] = decimal.Decimal(data['qty']) * decimal.Decimal(product.cost)
        year = data['date'].year
        try:
            latest_order = PurchaseOrder.objects.latest('id')
            split_array = latest_order.po_no.split('/')
            if int(split_array[1]) == year:
                no =  int(split_array[2]) +1
            else:
                no = 0
        except:
            no = 0
        data['po_no'] = "PO/"+str(year)+"/"+str(no)
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            my_order = PurchaseOrder.objects.latest('id')
            serializer = PurchaseOrderDetailSerializer(my_order)
            return Response(serializer.data)
        return Response(serializer.errors)




