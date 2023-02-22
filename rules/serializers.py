from rest_framework import serializers
from .models import PostReport 
from user.serializers import UserSerializer

class PostReportSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = PostReport
        fields = ['post' , 'reason' , 'reporter']
       
    
    def validate(self, attrs):
        print(attrs['reporter'])
        if PostReport.objects.filter(reporter = attrs['reporter'] , post = attrs['post']).exists():
            raise serializers.ValidationError({'error':'you cant submit a report on a post more than a time!'})
        return attrs