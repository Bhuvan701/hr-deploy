# Generated by Django 4.1 on 2022-11-30 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_resume', '0009_patent_journal_publication_conference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Approved',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Verified',
            new_name='verified',
        ),
    ]