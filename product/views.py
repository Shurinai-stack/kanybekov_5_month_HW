from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    list_of_category = CategoryListSerializer(instance=categories, many=True).data
    return Response(
        data=list_of_category,
        status=status.HTTP_200_OK,
    )

@api_view(['GET'])
def detail_category_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'error': 'Category not found'},
        )
    item = DetailCategorySerializers(instance=category, many=False).data
    return Response(
        data=item,
        status=status.HTTP_200_OK,
    )

@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    list_of_product = ProductListSerializer(instance=products, many=True).data
    return Response(
        data=list_of_product,
        status=status.HTTP_200_OK,
    )

@api_view(['GET'])
def detail_product_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'error': 'Product not found'},
        )
    item = DetailProductSerializers(instance=product, many=False).data
    return Response(
        data=item,
        status=status.HTTP_200_OK,
    )

@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    list_of_review = ReviewListSerializer(instance=reviews, many=True).data
    return Response(
        data=list_of_review,
        status=status.HTTP_200_OK,
    )

@api_view(['GET'])
def detail_review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'error': 'Review not found'},
        )
    item = DetailReviewSerializers(instance=review, many=False).data
    return Response(
        data=item,
        status=status.HTTP_200_OK,
    )



