from rest_framework import serializers
from .models import Test


class TestSerializers(serializers.Serializer):
    Test_Id = serializers.CharField(max_length=25)
    Name = serializers.CharField(max_length=25)

    def create(self, validated_data):
        return Test.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.Test_Id = validated_data.get('Test_Id', instance.Test_Id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.save()
        return instance

