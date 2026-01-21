from rest_framework.decorators import api_view, APIView
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from users.permissions import IsModerator


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

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewSerializer
        
        if self.action == 'retrieve':
            return 
        
        return ReviewValidateSerializer

@api_view(['GET'])
def products_with_reviews_api_view(request):
    pass