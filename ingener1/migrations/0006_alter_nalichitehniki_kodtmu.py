# Generated by Django 4.1.1 on 2023-06-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingener1', '0005_alter_nalichitehniki_kabinet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nalichitehniki',
            name='kodTMU',
            field=models.IntegerField(max_length=60, null=50, verbose_name='КодТМУ'),
        ),
    ]
