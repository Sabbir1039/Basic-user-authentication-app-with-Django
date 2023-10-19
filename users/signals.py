from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # elif hasattr(instance, 'profile'):
    #     instance.profile.save()
        
@receiver(post_save, sender=User)
def profile_save(sender, instance, *args, **kwargs):
    instance.profile.save() 
        