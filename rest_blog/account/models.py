from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  note = models.CharField(max_length=200)
  twitter = models.CharField(max_length=200)

  def __str__(self):
    return self.user.username

@receiver(post_save, sender = User)
def create_user_profile( sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
  
  try:
        instance.profile.save()
  except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

