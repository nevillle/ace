from rest_framework import serializers
from .models import *
from register.serializers import CompanySerializer
from products.serializers import ProductSerializer



class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = '__all__'



class PurchaseOrderDetailSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField("get_product")
    comapny = serializers.SerializerMethodField("get_comapny")

    class Meta:
        model = PurchaseOrder
        fields = '__all__'


    def get_product(self, obj):
        return ProductSerializer.get_serialized(obj.product)

    def get_comapny(self, obj):
        return CompanySerializer.get_serialized(obj.comapny)




