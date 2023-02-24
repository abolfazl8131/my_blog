from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def profimage_image_directory_path(instance, filename):
  
    
    return 'img_{0}/{1}'.format(instance.id, filename)

class Author(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    description = models.TextField( null=True )
    image = models.ImageField(upload_to=profimage_image_directory_path , default='default.jpg')
    def __str__(self) -> str:
        return f'{self.user}'