# Generated by Django 4.1 on 2022-10-06 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_profile_delete_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]