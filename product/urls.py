from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('products', views.ProductViewSet, basename='product')
router.register('reviews', views.ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path('products/reviews/', views.products_with_reviews_api_view),
]
