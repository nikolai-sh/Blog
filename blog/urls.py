from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                    CategoryPostDetailView,
                    UserPostListView
                    )


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<int:pk>/<str:name>/', CategoryPostDetailView.as_view(), name='posts-category'),
]
