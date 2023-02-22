from django.db import models
from blog.models import Post , User
# Create your models here.


class ReportPriority(models.TextChoices):
    SPAM = 'SPM' , 'Spam'


class PostReport(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    reporter = models.ForeignKey(User , on_delete=models.PROTECT)
    reason = models.CharField(max_length=100,default='SPM' , choices=ReportPriority.choices)

    def __str__(self) -> str:
        return f'{self.post.title} - {self.reason}'

    
