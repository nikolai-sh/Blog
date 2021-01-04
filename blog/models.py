from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """ Model for category of our Post (e.g. Sport, Fashion etc.) """

    name = models.CharField(max_length=100, help_text="Write a category for post (e.g. Sport, Fashion etc.)")

    def __str__(self):
        return self.name






class Post(models.Model):
    """ Model for our posts """

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Post
        """
        return reverse("post-detail", kwargs={"pk": self.pk})