from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import MovieMiniSerializer, MovieSerializer
from .models import Movie
from djangocrud.api import serializers
from rest_framework.response import Response

# View Creation
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)
