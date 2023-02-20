from .views import PostListViewSet , PostDetailViewSet , CommentViewSet , CommentDetailViewSet , CommentDeleteAPIView
from django.urls import path , include
from rest_framework.routers import DefaultRouter
# Create a router and register our viewsets with it.

router = DefaultRouter()
router.register(r'posts', PostListViewSet,basename="post-list")
router.register(r'post', PostDetailViewSet,basename="post-detail")
router.register(r'comment-create' , CommentViewSet , basename='comment-create')
router.register(r'comments' , CommentDetailViewSet , basename='comment-detail')
urlpatterns = [

    path('', include(router.urls)),
  
    path('comment/delete/<int:pk>/' , CommentDeleteAPIView.as_view( http_method_names = ['delete']))
    
    
] 
