# Generated by Django 2.2.1 on 2019-07-31 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0023_auto_20190731_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]