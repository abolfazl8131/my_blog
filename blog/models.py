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
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50 , unique=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(null=True)
    img = models.ImageField()
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

    def verify(self):
        
        if self.objects.groupby(self.user,  self.post).count() != 0:
            return False

    def __str__(self) -> str:
        return f'{self.post.slug}'

class ReportPriority(models.TextChoices):
    SPAM = 'SPM' , 'Spam'



class PostReport(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    reporter = models.ForeignKey(User , on_delete=models.PROTECT)
    reason = models.CharField(max_length=100,default='SPM' , choices=ReportPriority.choices)

    def __str__(self) -> str:
        return f'{self.post.title} - {self.reason}'
