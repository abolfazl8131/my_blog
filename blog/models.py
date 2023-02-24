from django.db import models
from user.models import Author , User

# Create your models here.
class ThingPriority(models.IntegerChoices):
    LOW = 1, 'Low'
    NR = 2, 'NotRecommended'
    Normal = 3, 'Normal'
    R = 4 , 'Recommended'
    HR = 5 , 'HighlyRecommended'



class Category(models.Model):
  
    title = models.CharField(max_length=50 , unique=True)

    def __str__(self) -> str:
        return f'{self.title}'

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'img_{0}/{1}'.format(instance.id, filename)



class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(null=True)
    img = models.ImageField(upload_to=user_directory_path , null=True)
    body = models.TextField()
    author = models.ForeignKey(Author , on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category)
    show = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f'{self.title}'
    
   

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.PROTECT)
    body = models.TextField()
    post = models.ForeignKey(Post,  on_delete=models.PROTECT)
    rating = models.IntegerField(default=None, choices=ThingPriority.choices,null=True)
    show = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now_add=True , blank=True , null=True)


    def __str__(self) -> str:
        return f'{self.post.slug}'  
    
    def show_filter(self):
        return self.objects.filter(show=True)
    
   