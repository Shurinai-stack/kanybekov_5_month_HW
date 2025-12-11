from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Review
from .serializers import *

@api_view(['GET', 'POST'])
def category_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategoryListSerializer(categories, many=True).data
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    
    elif request.method == 'POST':
        name = request.data.get("name")

        category = Category.objects.create(name=name)

        return Response(
            data=DetailCategorySerializers(category).data,
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
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
        category.name = request.data.get("name")
        category.save()

        return Response(
            data=DetailCategorySerializers(category).data,
            status=status.HTTP_200_OK
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
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")
        category_id = request.data.get("category")

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
        product.title = request.data.get("title")
        product.description = request.data.get("description")
        product.price = request.data.get("price")
        product.category_id = request.data.get("category")
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
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'POST':
        product_id = request.data.get("product")
        text = request.data.get("text")
        stars = request.data.get("stars")

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
        review.text = request.data.get("text")
        review.stars = request.data.get("stars")
        review.product_id = request.data.get("product")
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
