from __future__ import absolute_import,unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from . models import profile
from celery.schedules import crontab

@shared_task
def send_email(name):
	mail = profile.objects.filter(aadhar=name).first()
	send_mail(
			'',
			'your resume got shortlisted',
			settings.EMAIL_HOST,
			[mail.email]
		)
