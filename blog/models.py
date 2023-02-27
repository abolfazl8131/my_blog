from django.db import models
from user.models import Author , User
from .managers import PublishedManager
# Create your models here.
class ThingPriority(models.IntegerChoices):
    LOW = 1, 'Low'
    NR = 2, 'NotRecommended'
    Normal = 3, 'Normal'
    R = 4 , 'Recommended'
    HR = 5 , 'HighlyRecommended'



class Category(models.Model):
  
    title = models.CharField(max_length=50 , unique=True)

    class Meta:
        verbose_name = 'موضوع'
       
        verbose_name_plural = "موضوعات"

    def __str__(self) -> str:
        return f'{self.title}'

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'img_{0}/{1}'.format(instance.id, filename)



class Post(models.Model):
    slug = models.SlugField(verbose_name='اسلاگ')
    title = models.CharField(max_length=100 , verbose_name='موضوع')
    date_published = models.DateTimeField(auto_now_add=True  , verbose_name='تاریخ انتشار')
    last_update = models.DateTimeField(null=True , verbose_name='اخرین بروز رسانی')
    img = models.ImageField(upload_to=user_directory_path , null=True, verbose_name='عکس')
    body = models.TextField(verbose_name='بدنه')
    author = models.ForeignKey(Author , on_delete=models.PROTECT , verbose_name='نویسنده')
    categories = models.ManyToManyField(Category  , verbose_name='موضوعات')
    show = models.BooleanField(default=True , verbose_name='نمایش')

    objects = models.Manager()

    published = PublishedManager()

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = "پستها"

    def __str__(self) -> str:
        return f'{self.title}'
    
   

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
    
    
    
   