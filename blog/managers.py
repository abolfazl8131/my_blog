from django.db import models

class PublishedManager(models.Manager):
      
    def get_queryset(self , *args,  **kwargs):
        return super(PublishedManager , self).get_queryset().filter(show=True)