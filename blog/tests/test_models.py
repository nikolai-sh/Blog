from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import Category, Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Post.objects.create(title='Some post', 
                    author=User.objects.create(username='Bill'), 
                    content='Post content with a lot of words.',
                    category=Category.objects.create(name='Sport'))

    def test_title_max_length(self):
        title = Post.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)