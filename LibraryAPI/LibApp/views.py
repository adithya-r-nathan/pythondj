from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from LibApp.models import Genres,Books
from LibApp.serializers import GenreSerializer,BookSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def genreApi(request,id=0):
    if request.method=='GET':
        genres = Genres.objects.all()
        genre_serializer = GenreSerializer(genres, many=True)
        return JsonResponse(genres_serializer.data, safe=False)

    elif request.method=='POST':
        genre_data=JSONParser().parse(request)
        genre_serializer = GenreSerializer(data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        genre_data = JSONParser().parse(request)
        genre=Genres.objects.get(GenreId=genre_data['GenreId'])
        genre_serializer=GenreSerializer(genre,data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        genre=Genres.objects.get(genreId=id)
        genre.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def bookApi(request,id=0):
    if request.method=='GET':
        books = Books.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)

    elif request.method=='POST':
        book_data=JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        book_data = JSONParser().parse(request)
        book=Books.objects.get(bookId=book_data['bookId'])
        book_serializer=BookSerializer(book,data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        book=Books.objects.get(bookId=id)
        book.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)



