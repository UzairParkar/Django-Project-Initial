from rest_framework import serializers
from quickstart.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    # def validate_place(self,value):
    #     if not isinstance(value,str):
    #         raise serializers.ValidationError({"message":"must be a string"})
    #     return value
