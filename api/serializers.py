from rest_framework import serializers
from .models import ApiPost, ApiProfile

class ApiPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiPost
        fields = ('title', 'profile', 'image', 'description', 'posted_at', 'link',)


class ApiProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiProfile
        fields = ('user', 'profile_picture', 'bio',)