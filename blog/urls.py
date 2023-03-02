from blog.views.post_views import PostListViewSet , PostDetailViewSet ,PostCreateAPIView,GetCategoryAPIView , PostUpdateAPIView
from blog.views.comment_views import CommentDeleteAPIView , CommentDetailViewSet , CommentViewSet
from django.urls import path , include
from rest_framework.routers import DefaultRouter
# Create a router and register our viewsets with it.
from django.views.decorators.csrf import ensure_csrf_cookie , csrf_exempt

router = DefaultRouter()
router.register(r'posts', PostListViewSet,basename="post-list")
router.register(r'post', PostDetailViewSet,basename="post-detail")
router.register(r'comment-create' , CommentViewSet , basename='comment-create')
router.register(r'comments' , CommentDetailViewSet , basename='comment-detail')
urlpatterns = [

    path('', include(router.urls)),
  
    path('comment/delete/<int:pk>/' , CommentDeleteAPIView.as_view( http_method_names = ['delete'])),
    path('new-post/' ,PostCreateAPIView.as_view()),
    path('categories/all/' , GetCategoryAPIView.as_view() ),
    path('post/<int:id>/update/' ,PostUpdateAPIView.as_view() )
    
    
] 
