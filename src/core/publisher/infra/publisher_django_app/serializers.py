from rest_framework import serializers
from core.publisher.infra.publisher_django_app.models import Publisher


class CreatePublisherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)

    # def create(self, validated_data):
    #     return Publisher.objects.create(**validated_data)
    


class CreatePublisherResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)


class ListPublisherSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    is_active = serializers.BooleanField()
    
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass