from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Containers, EcoShop, TipsTricks, Location
from .serializers import CategorySerializer, ContainersSerializer, EcoShopSerializer, TipsTricksSerializer, LocationSerializer


class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        containers = Containers.objects.all()

        categories_serializer = CategorySerializer(categories, many=True)
        containers_serializer = ContainersSerializer(containers, many=True)

        data = {
            "categories": categories_serializer.data,
            "containers": containers_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContainersListView(APIView):
    def get(self, request, *args, **kwargs):
        containers = Containers.objects.all()
        serializer = ContainersSerializer(containers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContainersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationListView(APIView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EcoShopListView(APIView):
    def get(self, request, *args, **kwargs):
        eco_shops = EcoShop.objects.all()
        serializer = EcoShopSerializer(eco_shops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EcoShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipsTricksListView(APIView):
    def get(self, request, *args, **kwargs):
        tips_tricks = TipsTricks.objects.all()
        serializer = TipsTricksSerializer(tips_tricks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TipsTricksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)