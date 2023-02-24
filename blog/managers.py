from django.db import models

class PostManager(models.Manager):
      
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(show = True)
        return queryset    