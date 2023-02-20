from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    description = models.TextField( null=True )
    def __str__(self) -> str:
        return f'{self.user}'