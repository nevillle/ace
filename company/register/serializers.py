from rest_framework import serializers
from .models import *
import json
from rest_framework.renderers import JSONRenderer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def get_serialized(obj):
        serialized_data = CompanySerializer(obj).data
        return json.loads(JSONRenderer().render(serialized_data))

