from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """ Model for category of our Post (e.g. Sport, Fashion etc.)
        Our posts can have only one category.
    """

    name = models.CharField(verbose_name="category", max_length=100, help_text="Write a category for post (e.g. Sport, Fashion etc.)")

    class Meta: 
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Post(models.Model):
    """ Model for our posts """

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_posted']


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Post
        """
        return reverse("post-detail", kwargs={"pk": self.pk})