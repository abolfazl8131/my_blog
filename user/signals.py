from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver
from .models import Author , User


@receiver(post_save, sender=User)
def author_handler(sender, instance,**kwargs):
    try:
        Author.objects.create(user=instance)
    except:
        pass