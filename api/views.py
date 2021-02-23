from rest_framework import generics

from books.models import Book

from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializers_class = BookSerializer