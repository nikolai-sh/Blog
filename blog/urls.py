from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                    CategoryPostDetailView
                    )


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<int:pk>/<str:name>/', CategoryPostDetailView.as_view(), name='posts-category'),
]
