# Generated by Django 2.2.1 on 2019-10-09 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0047_auto_20191009_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]