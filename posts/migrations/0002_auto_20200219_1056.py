# Generated by Django 2.2.7 on 2020-02-19 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='profile',
            new_name='author',
        ),
    ]
