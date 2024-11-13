# blog/urls.py
from django.urls import path
from .views import RegisterView, LoginView, PostViewSet, CommentViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # Post-related endpoints
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),

    # Comment-related endpoints (nested under posts)
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view({'delete': 'destroy'}), name='comment-detail'),
]
