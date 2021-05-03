from rest_framework import serializers
from LibApp.models import Genres, Books

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('GenreId',
                  'GenreName')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('BookId',
                  'BookName',
                  'Availability',
                  'Author',
                  'ReturnDate')
                  