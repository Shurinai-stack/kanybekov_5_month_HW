from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from users.permissions import IsModerator
from users.validators import validate_user_age

from .models import Category, Product, Review
from .serializers import *


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        
        if self.action == 'retrieve':
            return DetailProductSerializers
        
        return CategoryValidateSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsModerator]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        
        if self.action == 'retrieve':
            return DetailProductSerializers
        
        return ProductValidateSerializer

    def perform_create(self, serializer):
        validate_user_age(self.request)
        serializer.save()


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewSerializer
        
        if self.action == 'retrieve':
            return ReviewSerializer
        
        return ReviewValidateSerializer


@api_view(['GET'])
def products_with_reviews_api_view(request):
    pass
