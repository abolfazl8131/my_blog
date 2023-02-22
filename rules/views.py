from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import PostReportSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ReportSubmitAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated , )
    serializer_class = PostReportSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        
        _mutable = data._mutable
        
        data._mutable = True
        
        data['reporter'] = request.user.id

        data._mutable = _mutable
        
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)