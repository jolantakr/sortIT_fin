from rest_framework import serializers
from .models import Category, Type


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "image", "detail1_name", "detail1_description", "detail2_name", "detail2_description", "detail3_name", "detail3_description"]

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "name"]