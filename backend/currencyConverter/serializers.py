from rest_framework import serializers
from .models import CurrencyRateRequest


class CurrencyRateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRateRequest
        fields = '__all__'
