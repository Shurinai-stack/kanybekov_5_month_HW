from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Review
from .serializers import *

@api_view(['GET', 'POST'])
def category_list_create_api_view(request):
    serializer = CategoryValidateSerializer(data=request.data)
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategoryListSerializer(categories, many=True).data
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
        
    elif request.method == 'POST':
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data= serializer.errors
            )
        name = serializer.validated_data.get("name")
        category = Category.objects.create(name=name)

        return Response(
            data=DetailCategorySerializers(category).data,
            status=status.HTTP_201_CREATED
        )

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    serializer = CategoryValidateSerializer(data=request.data)
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            data={'error': 'Category not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        return Response(
            data=DetailCategorySerializers(category).data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'PUT':
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
        category.name = serializer.validated_data.get("name")
        category.save()

        return Response(
            data=DetailCategorySerializers(category).data,
            status=status.HTTP_200_OK,
        )

    elif request.method == 'DELETE':
        category.delete()

        return Response(
            data={'message': 'Category deleted'},
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductListSerializer(products, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data = serializer.errors
            )
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description")
        price = serializer.validated_data.get("price")
        category_id = serializer.validated_data.get("category_id")

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id
        )

        return Response(
            data=DetailProductSerializers(product).data,
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            data={"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        return Response(
            data=DetailProductSerializers(product).data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data =request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data = serializer.errors
            )
        
        product.title = serializer.validated_data.get("title")
        product.description = serializer.validated_data.get("description")
        product.price = serializer.validated_data.get("price")
        product.category_id = serializer.validated_data.get("category_id")
        product.save()

        return Response(
            data=DetailProductSerializers(product).data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'DELETE':
        product.delete()

        return Response(
            data={'message': 'Product deleted'},
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    serializer = ReviewValidateSerializer(data=request.data)
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'POST':
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
        product_id = serializer.validated_data.get("product_id")
        text = serializer.validated_data.get("text")
        stars = serializer.validated_data.get("stars")

        review = Review.objects.create(
            product_id=product_id,
            text=text,
            stars=stars
        )

        return Response(
            data=ReviewSerializer(review).data,
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    serializer = ReviewValidateSerializer(data=request.data)
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={"error": "Review not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        return Response(
            data=ReviewSerializer(review).data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'PUT':
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
        review.text = serializer.validated_data.get("text")
        review.stars = serializer.validated_data.get("stars")
        review.product_id = serializer.validated_data.get("product_id")
        review.save()

        return Response(
            data=ReviewSerializer(review).data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'DELETE':
        review.delete()

        return Response(
            data={'message': 'Review deleted'},
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET'])
def products_with_reviews_api_view(request):
    products = Product.objects.all()

    result = []
    for product in products:
        reviews = Review.objects.filter(product=product)

        if reviews.exists():
            total = sum([r.stars for r in reviews])
            rating = total / reviews.count()
        else:
            rating = None

        data = ProductReviewSerializer(product).data
        data["rating"] = rating

        result.append(data)

    return Response(
        data=result,
        status=status.HTTP_200_OK
    )
