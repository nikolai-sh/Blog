from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post, Category
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )


class CategoryMixin(ContextMixin):
    """ Add all categories to context """  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    

class PostListView(ListView, CategoryMixin): 
    model = Post
    template_name = "blog/blog_home.html"
    context_object_name = 'posts'
    paginate_by = 5
   

class PostDetailView(DetailView, CategoryMixin):  
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView, CategoryMixin):
    model = Post
    fields = ['title', 'content', 'category', 'image']
    
    def form_valid(self, form):
        """ Setting the author before create post create form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView, CategoryMixin
                     ):
    model = Post
    fields = ['title', 'content', 'category', 'image']
    
    def form_valid(self, form):
        """ Setting the author before create post create form """
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        """ Check if user is author of post and return bool value """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     DeleteView, CategoryMixin
                     ):  
    model = Post
    success_url = '/' #redirect to home page after delete post

    def test_func(self):
        """ Check if user is author of post and return bool value """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CategoryPostDetailView(DetailView, CategoryMixin):
    model = Category
    template_name = "blog/posts_category.html" 


class UserPostListView(ListView, CategoryMixin ):  
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

