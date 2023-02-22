from .views import ReportSubmitAPIView
from django.urls import path , include



urlpatterns = [

    path('report/' , ReportSubmitAPIView.as_view())
    
    
] 
