from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile


def create_profile(sender,instance,created,**kwargs):
    if created:
        owner = instance
        profile = Profile(
            owner=owner,
            user_name=owner.username,
            name = owner.first_name,
            email = owner.email
        )
        profile.save()


def update_profile(sender,instance,created,**kwargs):
    profile = instance
    owner = profile.owner

    if created is False:
        owner.username = profile.user_name
        owner.first_name = profile.name
        owner.email = profile.email
        owner.save()


post_save.connect(create_profile,sender=User)
post_save.connect(update_profile,sender=Profile)