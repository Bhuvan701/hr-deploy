# Generated by Django 4.0.5 on 2022-09-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_resume', '0002_profile_image_alter_profile_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(max_length=30, null=True),
        ),
    ]