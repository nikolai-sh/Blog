import django
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import ContextMixin
from hitcount.views import HitCountDetailView
from django.contrib.auth.models import User
from blog.models import Post, Category
from comments.forms import CommentForm
from django.db.models import Q, query
from comments.models import Comment
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


    # def get_context_data(self, **kwargs):
    #     # def add_comment(self, request):
    #     #     if request.method == 'POST':
    #     #         comment_form = self.comment_form_class()
    #     #         if comment_form.is_valid():
    #     #             self.save(comment_form)
    #     #         return self.redirect('post-detail')     
        
    #     # comments_form = add_comment(self)
    #     context = super().get_context_data(**kwargs)
    #     context["comments_form"] = comments_form
    #     return context

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
   
        
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)