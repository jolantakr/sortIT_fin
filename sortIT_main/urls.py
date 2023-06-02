from django.urls import path
from sortIT_main import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('containers/', views.ContainersListView.as_view(), name='containers-list'),
    path('locations/', views.LocationListView.as_view(), name='location-list'),
    path('eco_shops/', views.EcoShopListView.as_view(), name='eco-shop-list'),
    path('tips_tricks/', views.TipsTricksListView.as_view(), name='tips-tricks-list'),
]
