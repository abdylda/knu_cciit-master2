# Generated by Django 4.1.1 on 2023-03-28 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
    ]
