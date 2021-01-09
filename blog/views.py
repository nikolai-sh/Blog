from blog.models import Post, Category
from django.shortcuts import render
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
        # context['most_popular_posts'] = Post.objects.order_by('visit_post')[:3] #TODO get three most popular posts
        return context
    

class PostDetailView(DetailView):
    model = Post
    

# class CategoryListView(ListView):
#     model = Category
#     template_name = "blog/blog_home.html"
#     context_object_name = 'categories'
#     print(Category.objects.all())