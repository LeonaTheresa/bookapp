# from django.shortcuts import render

# Create your views here.

# books/views.py

# books/views.py

from rest_framework import viewsets
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['title', 'author', 'genre']  # Fields to search
    ordering_fields = ['title', 'author', 'price']  # Fields to order
    ordering = ['title']  # Default ordering

