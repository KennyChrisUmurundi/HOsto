# Generated by Django 2.2.1 on 2019-08-01 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0024_auto_20190731_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]
