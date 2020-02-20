from django.shortcuts import render
from rest_framework import generics

from .models import ApiPost, ApiProfile
from .permissions import IsAuthorOrReadOnly
from .serializers import ApiPostsSerializer, ApiProfileSerializer
# Create your views here.
class ApiPostListView(generics.ListCreateAPIView):
    queryset = ApiPost.objects.all()
    serializer_class = ApiPostsSerializer

class ApiPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ApiPost.objects.all()
    serializer_class = ApiPostsSerializer



class ApiProfileListView(generics.ListCreateAPIView):
    queryset = ApiProfile.objects.all()
    serializer_class = ApiProfileSerializer

class ApiProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiProfile.objects.all()
    serializer_class = ApiProfileSerializer