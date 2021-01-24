from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import Category, Post

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(name='History')
    
    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'category')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Post.objects.create(title='Some post', 
                    author=User.objects.create(username='Bill'), 
                    content='Post content with a lot of words.',
                    category=Category.objects.create(name='Sport'))

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/1/')
