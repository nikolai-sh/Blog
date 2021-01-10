from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                    PostCreateView,
                    CategoryPostDetailView,
                    UserPostListView
                    )


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('category/<int:pk>/<str:name>/', CategoryPostDetailView.as_view(), name='posts-category'),
]
