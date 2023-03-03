from django.db import models
from user.models import User
from blog.managers import PublishedManager

from .post_models import Post , ThingPriority
 

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.PROTECT , verbose_name='کاربر')
    body = models.TextField(verbose_name='متن ')
    post = models.ForeignKey(Post,  on_delete=models.PROTECT , verbose_name='پست مربوطه')
    rating = models.IntegerField(default=None, choices=ThingPriority.choices,null=True , verbose_name='امتیاز')
    show = models.BooleanField(default=True  , verbose_name='نمایش')
    date_published = models.DateTimeField(auto_now_add=True , blank=True , null=True , verbose_name='تاریخ انتشار')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural= 'کامنت ها'

    def __str__(self) -> str:
        return f'{self.post.slug} - {self.user.username}'  
    
    
    
   