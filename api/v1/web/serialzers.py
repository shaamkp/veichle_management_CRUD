from rest_framework import serializers
from web.models import VeichleDetails


class AddVeichleDetailsSerializer(serializers.Serializer):
    number = serializers.CharField()
    veichle_type = serializers.CharField()
    model = serializers.CharField()
    description = serializers.CharField()


class ViewVeichleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeichleDetails
        fields = (
            'id',
            'number',
            'veichle_type',
            'model',
            'description',
        )