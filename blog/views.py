from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def home(request):
    return render(request, 'blog/blog_home.html')

class PostListView(ListView):
    
    model = Post
    template_name = "blog/blog_home.html"
    ordering = ['-date_posted']
    context_object_name = 'posts'
    paginate_by = 5