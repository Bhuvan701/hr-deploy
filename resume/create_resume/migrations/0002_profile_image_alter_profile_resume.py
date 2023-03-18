# Generated by Django 4.0.5 on 2022-09-25 13:33

import create_resume.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, storage=create_resume.models.OverwriteStorage, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(storage=create_resume.models.OverwriteStorage, upload_to='resumes/'),
        ),
    ]
