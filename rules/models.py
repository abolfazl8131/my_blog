from django.db import models
from blog.models import Post , User
# Create your models here.


class ReportPriority(models.TextChoices):
    SPAM = 'SPM' , 'Spam'


class PostReport(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT , verbose_name='پست')
    reporter = models.ForeignKey(User , on_delete=models.PROTECT , verbose_name='گزارش دهنده')
    reason = models.CharField(max_length=100,default='SPM' , choices=ReportPriority.choices , verbose_name='دلیل گزارش')

    class Meta:
        verbose_name = 'گزارش پست'
        verbose_name_plural = 'گزارشات پست'

    def __str__(self) -> str:
        return f'{self.post.slug} - {self.reason}'

    
