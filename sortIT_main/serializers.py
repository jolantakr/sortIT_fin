from rest_framework import serializers
from .models import Category, Containers, Location


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "image", "detail1_name", "detail1_description", "detail2_name", "detail2_description",
                  "detail3_name", "detail3_description"]


class ContainersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Containers
        fields = ["id", "title", "image", "detail1_name", "detail1_description", "detail2_name", "detail2_description",
                  "detail3_name", "detail3_description"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name", "contact", "street", "city", "state", "country", "latitude", "longitude"]