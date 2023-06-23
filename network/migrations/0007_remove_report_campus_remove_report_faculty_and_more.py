# Generated by Django 4.1.1 on 2023-03-19 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('network', '0006_remove_transfernetwork_namkabinet_report_namkabinet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='report',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='report',
            name='kabinet',
        ),
        migrations.RemoveField(
            model_name='report',
            name='namKabinet',
        ),
        migrations.AddField(
            model_name='report',
            name='reportitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Рапорт на подразделение'),
        ),
        migrations.AddField(
            model_name='transfernetwork',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='txst_key1', to='main.campus', verbose_name='Корпус'),
        ),
        migrations.AddField(
            model_name='transfernetwork',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_key', to='main.faculty', verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='transfernetwork',
            name='kabinet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_key', to='main.kabinet', verbose_name='Кабинет'),
        ),
        migrations.AddField(
            model_name='transfernetwork',
            name='namKabinet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_key', to='main.namkabinet', verbose_name='Название кабинета'),
        ),
    ]