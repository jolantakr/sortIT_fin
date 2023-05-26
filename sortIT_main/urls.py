from django.urls import path
from sortIT_main import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
