# Generated by Django 2.2.1 on 2019-10-03 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0043_auto_20191002_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]
