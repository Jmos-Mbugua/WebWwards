from rest_framework import serializers
from .models import Post, Profile

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'profile', 'image', 'description', 'posted_at', 'link',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_picture', 'bio',)