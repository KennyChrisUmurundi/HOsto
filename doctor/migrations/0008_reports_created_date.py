# Generated by Django 2.2.1 on 2019-06-18 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20190617_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]