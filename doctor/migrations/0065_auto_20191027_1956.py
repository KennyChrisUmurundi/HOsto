# Generated by Django 2.2.1 on 2019-10-27 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0064_auto_20191016_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructionsforpharmacy',
            name='days',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructionsforpharmacy',
            name='drug_name',
            field=models.CharField(default='panadol', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructionsforpharmacy',
            name='instructions',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='prices',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='diagnosis',
            field=models.CharField(max_length=300),
        ),
    ]