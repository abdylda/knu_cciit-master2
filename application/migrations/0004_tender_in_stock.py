# Generated by Django 4.1.1 on 2023-03-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_tender_purchase_order_is_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='in_stock',
            field=models.BooleanField(default=False, verbose_name='На складе'),
        ),
    ]
