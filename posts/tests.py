from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post, Profile
# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username= 'testuser1', password='testuser123')
        testuser1.save()

        test_post = Post.objects.create(title=testuser1, profile='Blog title', decription='Body content...')
        test_post.save()

    def test_post_content(self):
