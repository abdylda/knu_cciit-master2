# Generated by Django 4.1.1 on 2023-03-19 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('network', '0004_remove_transfernetwork_faculty_report_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='reportitle',
        ),
        migrations.RemoveField(
            model_name='transfernetwork',
            name='kabinet',
        ),
        migrations.AddField(
            model_name='report',
            name='kabinet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_key', to='main.kabinet', verbose_name='Кабинет'),
        ),
    ]
