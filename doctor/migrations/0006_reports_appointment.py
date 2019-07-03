# Generated by Django 2.2.1 on 2019-06-17 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0005_auto_20190617_1152'),
        ('doctor', '0005_auto_20190617_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='appointment',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='reception.Appointment'),
            preserve_default=False,
        ),
    ]
