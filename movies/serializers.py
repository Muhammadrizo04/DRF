from rest_framework import serializers

from .models import Movie, Review

class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""
    class Meta:
        model = Movie
        fields = ("title", "tagline", "category",)



class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление одзыва"""

    class Meta:
        model = Review
        fields = "__all__"

class MovieDetailSerializer(serializers.ModelSerializer):
    """Полный фильмов"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    reviews = ReviewCreateSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ("draft", )