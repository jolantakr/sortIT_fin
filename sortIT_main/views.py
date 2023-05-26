from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sortIT_main.models import Category, Type
from sortIT_main.serializers import CategorySerializer, TypeSerializer


class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        types = Type.objects.all()

        categories_serializer = CategorySerializer(categories, many=True)
        types_serializer = TypeSerializer(types, many=True)

        data = {
            "categories": categories_serializer.data,
            "types": types_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        title = request.POST.get('title')
        image = request.FILES.get('image')
        detail1_name = request.POST.get('detail1_name')
        detail1_description = request.POST.get('detail1_description')
        detail2_name = request.POST.get('detail2_name')
        detail2_description = request.POST.get('detail2_description')
        detail3_name = request.POST.get('detail3_name')
        detail3_description = request.POST.get('detail3_description')

        category = Category.objects.create(
            title=title,
            image=image,
            detail1_name=detail1_name,
            detail1_description=detail1_description,
            detail2_name=detail2_name,
            detail2_description=detail2_description,
            detail3_name=detail3_name,
            detail3_description=detail3_description
        )

        return Response(status=status.HTTP_201_CREATED)
