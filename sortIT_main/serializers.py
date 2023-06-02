from rest_framework import serializers
from .models import Category, Containers, Location, EcoShop, TipsTricks


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


class EcoShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcoShop
        fields = ["id", "title", "image", "detail1_description"]


class TipsTricksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipsTricks
        fields = ["id", "title", "image", "detail1_description"]