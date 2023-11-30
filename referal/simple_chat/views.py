from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import * 
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.
# Create your views here.

class PostListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CommentListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
