from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.db.models.signals import post_delete,post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.utils import timezone
class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name,max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
# Create your models here.

class profile(models.Model):
	name = models.CharField(max_length=50)
	department = models.CharField(max_length=30,null=True)
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	aadhar = models.IntegerField(null=True)
	resume = models.FileField(upload_to = 'resumes/',storage=OverwriteStorage)
	created_at = models.DateTimeField(default=timezone.now,null=True)
	viewed = models.BooleanField(default = False)
	short_listed = models.BooleanField(default=False)
	verified  = models.BooleanField(default=False)
	forward = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)
	appointed_date = models.DateTimeField(null=True)
	
	def delete(self, using=None, keep_parents=False):
		self.resume.storage.delete(self.resume.name)
		super().delete()
	
	def __str__(self):
		return f'{self.name} resume'


class staff(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	department = models.CharField(max_length=10)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			staff.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.staff.save()

	def __str__(self):
		return self.user.username 

class jobvacancy(models.Model):
	dept = models.CharField(max_length=20)
	noofvacancy = models.IntegerField()
	role = models.CharField(max_length=30)

	def __str__(self):
		return self.role 


class journal_publication(models.Model):
	name = models.ForeignKey(profile,on_delete = models.CASCADE)
	author = models.CharField(max_length = 100)
	title  = models.CharField(max_length=1000)
	journal_name = models.CharField(max_length=1000)
	indexed = models.BooleanField(default=False)
	unindexed = models.BooleanField(default=False)
	def __str__(self):
		return self.name.name


class conference(models.Model):
	name = models.ForeignKey(profile,on_delete = models.CASCADE)
	author = models.CharField(max_length = 100)
	title  = models.CharField(max_length=1000)
	conference_name = models.CharField(max_length=1000)

	def __str__(self):
		return self.name.name

class patent(models.Model):
	name = models.ForeignKey(profile,on_delete = models.CASCADE)
	author = models.CharField(max_length = 100)
	title  = models.CharField(max_length=1000)
	status = models.CharField(max_length=1000)

	def __str__(self):
		return self.name.name

class Rejected(models.Model):
	aadhar = models.IntegerField()

	def __int__(self):
		return self.aadhar