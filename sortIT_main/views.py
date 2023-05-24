from django.views import View
from django.http import JsonResponse
from .models import Category


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        data = []
        for category in categories:
            category_data = {
                'id': category.id,
                'title': category.title,
                'image': category.image.url,
                'detail1': {
                    'name': category.detail1_name,
                    'description': category.detail1_description,
                },
                'detail2': {
                    'name': category.detail2_name,
                    'description': category.detail2_description,
                },
                'detail3': {
                    'name': category.detail3_name,
                    'description': category.detail3_description,
                },
            }
            data.append(category_data)
        return JsonResponse(data, safe=False)

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

        return JsonResponse({'message': 'Category added'}, status=201)
