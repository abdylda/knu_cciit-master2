# Generated by Django 4.1.1 on 2023-04-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_remove_employee_department_remove_employee_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='sur_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]
