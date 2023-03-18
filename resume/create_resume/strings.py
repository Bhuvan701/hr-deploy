from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from.models import profile
@receiver(post_delete, sender=profile)
def post_save_image(sender, instance, *args, **kwargs):
    try:
        instance.img.delete(save=False)
    except:
        pass
@receiver(models.signals.pre_save, sender=profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = profile.objects.get(pk=instance.pk).file
    except MediaFile.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)