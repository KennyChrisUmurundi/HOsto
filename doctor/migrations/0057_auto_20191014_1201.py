# Generated by Django 2.2.1 on 2019-10-14 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0056_auto_20191014_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allotment',
            old_name='number',
            new_name='room_number',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='number',
            new_name='room_number',
        ),
        migrations.AlterField(
            model_name='prices',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]
