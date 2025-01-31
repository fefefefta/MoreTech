from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account
from ..management.models import Payment


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
