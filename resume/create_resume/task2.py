from __future__ import absolute_import,unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from . models import profile
from celery.schedules import crontab
import csv, smtplib, ssl
'''
@shared_task
def send_email(name):
	mail = profile.objects.filter(phone=name).first()
	send_mail(
			'',
			'your resume got shortlisted',
			settings.EMAIL_HOST,
			[mail.email]
		)
'''
@shared_task
def send_email(name):
	mail = profile.objects.filter(phone=name).first()
	message = """your resume got shorlisted """
	from_address = "your mail"
	password = 'pass'
	email=mail.email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(from_address, password)
	    server.sendmail(
	        from_address,
	        email,
	        msg=message
	    )