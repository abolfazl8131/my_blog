from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import PostReportSerializer
from rest_framework.response import Response
from rest_framework import status
from rules.models import PostReport
from rest_framework import serializers
# Create your views here.

class ReportSubmitAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated , )
    serializer_class = PostReportSerializer

    def perform_create(self, serializer):
        
        if PostReport.objects.filter(reporter = self.request.user , post = self.request.data['post']).exists():
            raise serializers.ValidationError({'error':'you cant submit a report on a post more than a time!'})
        serializer.save(reporter = self.request.user)
      
    