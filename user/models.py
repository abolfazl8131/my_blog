from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def profimage_image_directory_path(instance, filename):
  
    
    return 'img_{0}/{1}'.format(instance.id, filename)

class Author(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT, verbose_name='کاربر' )
    description = models.TextField( null=True ,  verbose_name='درباره خودتون' )
    image = models.ImageField(upload_to=profimage_image_directory_path , default='default.jpg' , verbose_name='عکس پروفایل')
    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'

    def __str__(self) -> str:
        return f'{self.user}'

    