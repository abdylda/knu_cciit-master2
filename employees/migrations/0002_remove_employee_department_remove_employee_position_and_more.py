# Generated by Django 4.1.1 on 2023-04-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.AddField(
            model_name='employee',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AddField(
            model_name='employee',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
    ]
