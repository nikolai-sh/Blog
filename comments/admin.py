from django.contrib import admin

from blog.models import Post
from .models import Comment

admin.site.register(Comment)