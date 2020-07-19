from rest_framework import serializers
from .models import *
import json
from rest_framework.renderers import JSONRenderer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def get_serialized(obj):
        serialized_data = ProductSerializer(obj).data
        return json.loads(JSONRenderer().render(serialized_data))
