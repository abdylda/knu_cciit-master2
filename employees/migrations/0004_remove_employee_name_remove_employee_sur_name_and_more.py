# Generated by Django 4.1.1 on 2023-04-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_sur_name_alter_employee_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='sur_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='surname',
        ),
        migrations.AddField(
            model_name='employee',
            name='Full_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО'),
        ),
    ]
