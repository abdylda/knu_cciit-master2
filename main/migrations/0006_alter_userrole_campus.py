# Generated by Django 4.1.1 on 2023-04-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_kabinet_campus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='campus',
            field=models.ManyToManyField(related_name='user_role_campus_key', to='main.campus', verbose_name='Корпус'),
        ),
    ]