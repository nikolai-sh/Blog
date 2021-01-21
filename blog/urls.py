from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    CategoryPostDetailView,
                    UserPostListView,
                    SearchResultsView
                    )


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('category/<int:pk>/<str:name>/', CategoryPostDetailView.as_view(), name='posts-category'),
]
