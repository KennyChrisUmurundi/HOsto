# Generated by Django 2.2.1 on 2019-06-11 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20190611_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
