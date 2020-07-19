from django.urls import path, include
from . import views
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, \
    PostViewSet
from rest_framework import routers


app_name = 'api'
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'api/', include(router.urls)),
]