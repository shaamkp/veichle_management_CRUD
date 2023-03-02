from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AdminProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SuperAdminProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()