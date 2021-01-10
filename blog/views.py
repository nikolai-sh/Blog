from blog.models import Post, Category
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (ListView, 
                                  DetailView,
                                  )



class PostListView(ListView):
    
    model = Post
    template_name = "blog/blog_home.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context
    

class PostDetailView(DetailView):
   
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories  
        return context
    

class CategoryPostDetailView(DetailView):

    model = Category
    template_name = "blog/posts_category.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories      
        return context
    


class UserPostListView(ListView):
    
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context
  