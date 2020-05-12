from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from client.models import UserProfile, UserBank

@receiver(post_save, sender=User)
def save_user_instance(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user_id=instance)
        UserBank.objects.create(user_id=instance)