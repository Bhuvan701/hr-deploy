# Generated by Django 4.1 on 2022-12-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_resume', '0010_rename_approved_profile_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='appointed_date',
            field=models.DateTimeField(null=True),
        ),
    ]