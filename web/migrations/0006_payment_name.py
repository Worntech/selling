# Generated by Django 3.2.25 on 2024-05-29 23:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20240528_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
