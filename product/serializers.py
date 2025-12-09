from rest_framework import serializers
from .models import Category,Product,Review

class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'products_count')

    def get_products_count(self, obj):
        return Product.objects.filter(category=obj).count()

class DetailCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DetailProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    stars_display = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'text', 'stars', 'stars_display')

    def get_stars_display(self, obj):
        return '*' * obj.stars
    
class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only =True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'reviews', 'rating')