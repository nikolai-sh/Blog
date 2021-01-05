from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView



class PostListView(ListView):
    
    model = Post
    template_name = "blog/blog_home.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['most_popular_posts'] = Post.objects.order_by('visit_post')[:3] #TODO get three most popular posts
        return context