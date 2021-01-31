from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post, Category
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q, query
from hitcount.views import HitCountDetailView
from django.views.generic import (ListView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )


class SidebarMixin(ContextMixin):
    """ Add sidebar data to context """  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["popular_posts"] = Post.objects.order_by('-hit_count_generic__hits')[:3]
        return context
    

class PostListView(ListView, SidebarMixin): 
    model = Post
    template_name = "blog/blog_home.html"
    context_object_name = 'posts'
    paginate_by = 5
   

class PostDetailView(HitCountDetailView, SidebarMixin):  
    model = Post
    count_hit = True

class PostCreateView(LoginRequiredMixin, CreateView, SidebarMixin):
    model = Post
    fields = ['title', 'content', 'category', 'image']
    
    def form_valid(self, form):
        """ Setting the author before create post create form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView,SidebarMixin 
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
                     DeleteView,SidebarMixin 
                     ):  
    model = Post
    success_url = '/' #redirect to home page after delete post

    def test_func(self):
        """ Check if user is author of post and return bool value """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CategoryPostDetailView(HitCountDetailView, SidebarMixin):
    
    model = Category
    template_name = "blog/posts_category.html" 



class UserPostListView(ListView, SidebarMixin ):  
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class SearchResultsView(ListView, SidebarMixin):
    model = Post
    template_name = 'blog/search_results.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query))
   
        
    
        
        